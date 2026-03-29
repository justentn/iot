import socket
import json
from logger import Logger

log = Logger()

class HttpServer:
    def __init__(self, port: int = 80):
        self._port = port
        self._routes = {}

    def route(self, path: str, method: str = 'GET'):
        def decorator(func):
            self._routes[(method, path)] = func
            return func
        return decorator

    def start(self):
        addr = socket.getaddrinfo('0.0.0.0', self._port)[0][-1]
        s = socket.socket()
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(addr)
        s.listen(5)
        log.info('HttpServer', f'listening on port {self._port}')

        while True:
            conn, addr = s.accept()
            log.info('HttpServer', f'connection from {addr}')
            self._handle(conn)

    def _handle(self, conn):
        try:
            request = conn.recv(1024).decode()
            if not request:
                return

            lines = request.split('\r\n')
            method, path, _ = lines[0].split(' ')

            handler = self._routes.get((method, path))
            if handler:
                body = handler()
                self._send(conn, 200, body)
            else:
                self._send(conn, 404, {'error': 'not found'})
        except Exception as e:
            log.error('HttpServer', f'error: {e}')
            self._send(conn, 500, {'error': str(e)})
        finally:
            conn.close()

    def _send(self, conn, status: int, body: dict):
        payload = json.dumps(body)
        response = (
            f'HTTP/1.1 {status} OK\r\n'
            f'Content-Type: application/json\r\n'
            f'Content-Length: {len(payload)}\r\n'
            f'\r\n'
            f'{payload}'
        )
        conn.send(response.encode())