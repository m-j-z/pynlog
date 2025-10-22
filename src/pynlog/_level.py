from enum import StrEnum


class Level(StrEnum):
    """
    Defines the log levels used by the logger.
    """
    DEBUG = "DEBUG"
    INFO = "INFO"
    SUCCESS = "SUCCESS"
    WARNING = "WARNING"
    ERROR = "ERROR"