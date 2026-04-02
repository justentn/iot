from lib.gpio.pin_type import PinType
from machine import ADC, Pin

class PinWrapper:
    """A custom wrapper used to interface with GPIO / ADC pins."""
    id: int
    type: PinType
    _adc: ADC
    _pin: Pin
    _on_read: None

    def __init__(self, pin: int, type: PinType, on_read=None):
        self.id = pin
        self.type = type
        self._adc = None
        self._pin = None
        self._on_read = None
        self._init_pin()

    def __str__(self):
        return f'PinWrapper(pin={self.id}, type={self.type})'

    def __repr__(self):
        return f'PinWrapper(pin={self.id}, type={self.type})'

    def _init_pin(self):
        if self.type == PinType.ADC:
            self._init_adc_pin(self.id)
        elif self.type == PinType.GPIO_INPUT:
            self._init_gpio_input_pin(self.id)
        else:
            self._init_gpio_output_pin(self.id)

    def _init_adc_pin(self, pin: int):
        self._pin = Pin(pin)
        self._adc = ADC(self._pin)
        self._adc.atten(ADC.ATTN_11DB)
        self._adc.width(ADC.WIDTH_12BIT)

    def _init_gpio_input_pin(self, pin: int):
        self._pin = Pin(pin, Pin.IN, Pin.PULL_UP)

    def _init_gpio_output_pin(self, pin: int):
        self._pin = Pin(pin, Pin.OUT)

    def read(self) -> int:
        if self.type == PinType.ADC:
            value = self._adc.read()
        else:
            value = self._pin.value()
        
        if self._on_read:
            self._on_read(self.id, value)
        
        return value

    def toggle(self) -> int:
        """Toggles the GPIO pin from off/on.
        
        Returns:
            The state of the pin.
        """
        if self.type == PinType.GPIO_OUTPUT:
            state = not self._pin.value()
            self._pin.value(state)
            return state