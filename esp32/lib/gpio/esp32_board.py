from lib.gpio.pin_wrapper import PinWrapper
from logger import Logger
from lib.gpio.pin_type import PinType


class Esp32Board:
    """A singleton object that represents an ESP32 board.
    Initializes a gpio manager used to interface with ADC / GPIO pins
    """

    _instance = None
    pins: dict[int, PinWrapper]
    logger: Logger

    def __new__(cls, pins: list[PinWrapper] = None):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.pins = {}
            cls._instance.logger = Logger()
            for p in pins:
                pin_handler = PinWrapper(p.id, p.type)
                cls._instance.pins[pin_handler.id] = pin_handler

        pin_strs = ', '.join(
            [f'Pin(id={p.id}, type={PinType.name(p.type)}' for p in pins])
        cls._instance.logger.info(
            'Esp32Board', f'Initialized pins [{pin_strs}]')

        return cls._instance

    def get_pin_value(self, pin: int) -> int:
        """Gets the raw pin value

        Args:
            pin: The pin to retrieve the value for.
        Returns:
            The pins value.
        """

        handler = self._instance.pins.get(pin)
        if handler is None:
            self._instance.logger.error('Esp32Board', f'PIN {pin} not found')
            return -1
        return handler.read()

    def toggle_pin(self, pin: int) -> bool:
        """Toggles the pins state

        Args:
            pin: The pin to toggle.
        Returns:
            The current state of the pin
        """

        handler = self._instance.pins.get(pin)
        if handler is None:
            self._instance.logger.error('Esp32Board', f'PIN {pin} not found')
            return
        return handler.toggle()
