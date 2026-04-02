import time

DEBUG = 0
INFO = 1
WARN = 2
ERROR = 3

LEVEL_NAMES = {
    DEBUG: 'DEBUG',
    INFO: 'INFO',
    WARN: 'WARN',
    ERROR: 'ERROR',
}

class Logger:
    _instance = None

    def __new__(cls, level: int = INFO):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.level = level
        return cls._instance

    def _log(self, level: int, name: str, msg: str):
        if level >= self.level:
            t = time.localtime()
            timestamp = f'{t[0]}-{t[1]:02d}-{t[2]:02d} {t[3]:02d}:{t[4]:02d}:{t[5]:02d}'
            print(f'[{timestamp}] [{LEVEL_NAMES[level]}] [{name}] {msg}')

    def debug(self, name: str, msg: str):
        self._log(DEBUG, name, msg)

    def info(self, name: str, msg: str):
        self._log(INFO, name, msg)

    def warn(self, name: str, msg: str):
        self._log(WARN, name, msg)

    def error(self, name: str, msg: str):
        self._log(ERROR, name, msg)