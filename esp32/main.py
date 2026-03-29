from boot import connect_wifi
from lib.gpio.esp32_board import Esp32Board
from lib.gpio.constants import *
from lib.netio.http_server import HttpServer
from config import PINS
from lib.netio.routes import register_routes
import time
import _thread


esp32_board = Esp32Board(PINS)
start = time.ticks_ms()
server = HttpServer(port=80)

register_routes(server, esp32_board)
_thread.start_new_thread(server.start, ())

while True:
    elapsed = time.ticks_diff(time.ticks_ms(), start)
    seconds = elapsed // 1000
    minutes = seconds // 60
    hours = minutes // 60
    print(f'runtime: {hours:02d}:{minutes % 60:02d}:{seconds % 60:02d}')
    time.sleep(5)
