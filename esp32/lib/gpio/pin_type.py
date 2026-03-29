class PinType:
    ADC = 0
    GPIO_INPUT = 1
    GPIO_OUTPUT = 2

    @staticmethod
    def name(t: int) -> str:
        names = {0: 'ADC', 1: 'GPIO_INPUT', 2: 'GPIO_OUTPUT'}
        return names.get(t, 'UNKNOWN')
