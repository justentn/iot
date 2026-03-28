from pin_type import PinType
from machine import ADC, Pin


class PinWrapper:
    id: int
    type: PinType
    pin: Pin

    def __init__(self, pin: int, type: PinType):
        self.id = pin
        self.type = type
        self._init_pin()

    def _init_pin(self):
        if self.type == PinType.ADC:
            self._init_adc_pin(self.id)
        elif self.type == PinType.GPIO_INPUT:
            self._init_gpio_input_pin(self.id)
        else:
            self._init_gpio_output_pin(self.id)

    def _init_adc_pin(self, pin: int):
        self.pin = Pin(pin)
        self._adc = ADC(pin)
        self._adc.atten(ADC.ATTN_11DB)
        self._adc.width(ADC.WIDTH_12BIT)

    def _init_gpio_input_pin(self, pin: int):
        self.pin = Pin(pin, Pin.IN, Pin.PULL_UP)

    def _init_gpio_output_pin(self, pin: int):
        self.pin = Pin(pin, Pin.OUT)

    def read(self) -> int:
        pass
