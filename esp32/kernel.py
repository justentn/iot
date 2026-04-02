import _thread
from logger import Logger
from lib.gpio.esp32_board import Esp32Board
from lib.gpio.pin_wrapper import PinWrapper
from lib.netio.http_server import HttpServer
from lib.netio.routes import register_routes
from lib.netio.mqtt_client import MqttClient

logger = Logger()


class Kernel:
    """The kernel is the main processing object used to
    process incoming and outgoing data upstream."""
    _instance = None
    _board = None
    _mqtt_client = MqttClient()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False

        return cls._instance

    def __init__(self, pins: list[PinWrapper] = None):
        if not getattr(self, "_initialized", False):
            if pins is None:
                return

            self._board = Esp32Board(pins)
            self._init_http_server(self._board)
            self._init_mqtt_client()
            self._initialized = True
            logger.info("Kernel", "kernel started...")

    def _init_http_server(self, board):
        server = HttpServer(port=80)
        register_routes(server, board)
        _thread.start_new_thread(server.start, ())

    def _init_mqtt_client(self):
        _thread.start_new_thread(self._mqtt_client.try_connect, ())
