from enum import IntEnum


class Level(IntEnum):
    """
    Defines the log levels used by the logger.
    """
    DEBUG = 0
    INFO = 1
    SUCCESS = 2
    WARNING = 3
    ERROR = 4