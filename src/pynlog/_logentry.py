from dataclasses import dataclass
from datetime import datetime


from pynlog._level import Level


@dataclass
class LogEntry:
    """
    Data class which contains information of the log.
    """
    level: Level
    caller: str
    message: str

    time: datetime = datetime.now()