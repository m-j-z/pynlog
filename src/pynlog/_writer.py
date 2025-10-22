from abc import ABC, abstractmethod


class Writer(ABC):
    """
    A helper abstract class used by Log to write a message.

        Methods:
            write(message: str)
    """

    @abstractmethod
    def write(self, message: str) -> None:
        """
        The function used to write a log.
        """
        pass
