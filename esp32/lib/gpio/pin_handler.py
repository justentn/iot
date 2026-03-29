from machine import ADC, Pin
from logger import Logger
from lib.gpio.pin_type import PinType
from lib.gpio.pin_wrapper import PinWrapper


class PinHandler:
    """Class used to interface with a pin."""

    def __init__(self, pin: int, pin_type: PinType):
        self.id = pin
        self.type = pin_type
        self.pin = None
        self._init_pin(pin, pin_type)

    def _init_pin(self, pin: int, pin_type: PinType):
        if pin_type == PinType.ADC:
            adc = ADC(Pin(pin))
            adc.atten(ADC.ATTN_11DB)
            adc.width(ADC.WIDTH_12BIT)
            self.pin = adc
        elif pin_type == PinType.GPIO_INPUT:
            self.pin = Pin(pin, Pin.IN, Pin.PULL_UP)
        else:
            self.pin = Pin(pin, Pin.OUT)

    def get_pin_value(self) -> int:
        """Gets the pins value.

        Returns:
            The raw pin value.
        """
        if self.type == PinType.ADC:
            return self.pin.read()
        return self.pin.value()

    def toggle(self):
        """Toggles the pin state from HIGH to LOW or LOW to HIGH"""

        if self.type == PinType.GPIO_OUTPUT:
            self.pin.value(not self.pin.value())
