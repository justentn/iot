from boot import connect_wifi
from lib.gpio.esp32_board import Esp32Board
from lib.gpio.constants import *
from lib.netio.http_server import HttpServer
from config import PINS
import time


DRY = 4095   # raw value in dry air
WET = 1500   # raw value in water

esp32_board = Esp32Board(PINS)
start = time.ticks_ms()
server = HttpServer(port=80)

while True:
    elapsed = time.ticks_diff(time.ticks_ms(), start)
    seconds = elapsed // 1000
    minutes = seconds // 60
    hours = minutes // 60
    print(f'runtime: {hours:02d}:{minutes % 60:02d}:{seconds % 60:02d}')
    time.sleep(5)

# while True:
    # esp32_board.toggle_pin(GPIO_PIN_5)

    # raw = esp32_board.get_pin_value(ADC_PIN_36)
    # voltage = (raw / 4095) * 3.3
    # # convert to moisture percentage
    # moisture = (1 - (raw - WET) / (DRY - WET)) * 100
    # moisture = max(0, min(100, moisture))  # clamp 0-100

    # print(f'raw: {raw} | voltage: {voltage:.2f}v | moisture: {moisture:.1f}%')

    # time.sleep(5)
