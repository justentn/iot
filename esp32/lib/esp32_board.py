from pin_handler import PinHandler
from logger import Logger
from pin_type import PinType
from pin_wrapper import PinWrapper


class Esp32Board:
    """A singleton object that represents an ESP32 board.
    Initializes a gpio manager used to interface with ADC / GPIO pins
    """
    _instance = None
    pins: dict[int, PinHandler]
    logger: Logger

    def __new__(cls, pins: list[PinWrapper] = None):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.pins = {}
            cls._instance.logger = Logger()
            for p in pins:
                pin_handler = PinHandler(p.id, p.type)
                cls._instance.pins[pin_handler.id] = pin_handler
            cls._instance.logger.info('Esp32Board', 'ESP32 board initialized')
        print(f'stored pins: {list(cls._instance.pins.keys())}')  # ← add this
        return cls._instance

    def get_pin_value(self, pin: int) -> int:
        print(pin)
        handler = self._instance.pins.get(pin)
        if handler is None:
            self._instance.logger.error('Esp32Board', f'PIN {pin} not found')
            return -1
        return handler.get_pin_value()

    def toggle_pin(self, pin: int) -> None:
        handler = self._instance.pins.get(pin)
        if handler is None:
            self._instance.logger.error('Esp32Board', f'PIN {pin} not found')
            return
        handler.toggle()
