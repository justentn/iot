from logger import Logger

logger = Logger()


class Kernel:
    """A singleton class used to interface with the various pins and
    send data upstream."""

    _instance = None
    _board = 

    def __call__(cls):
        if cls not in cls._instance:
            cls._instance = super(Kernel, cls).__call__()
        return cls
