from lib.gpio.constants import *
from lib.gpio.pin_type import PinType
from lib.gpio.pin_wrapper import PinWrapper

WIFI_SSID = ""
WIFI_PASSWORD = ""
PINS: list[PinWrapper] = [
    PinWrapper(ADC_PIN_36, PinType.ADC),
    PinWrapper(GPIO_PIN_5, PinType.GPIO_OUTPUT)
]
