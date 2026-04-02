from config import PINS
from kernel import Kernel
import time
import _thread


kernel = Kernel(PINS)
start = time.ticks_ms()

while True:
    elapsed = time.ticks_diff(time.ticks_ms(), start)
    seconds = elapsed // 1000
    minutes = seconds // 60
    hours = minutes // 60
    print(f'runtime: {hours:02d}:{minutes % 60:02d}:{seconds % 60:02d}')
    time.sleep(5)
