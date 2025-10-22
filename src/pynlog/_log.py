from pynlog._formatter import Formatter
from pynlog._writer import Writer
from pynlog._consolewriter import ConsoleWriter
from pynlog._filewriter import FileWriter
from pynlog._level import Level
from pynlog._utility import get_caller
from pynlog._logentry import LogEntry

class Log:
    """
    A static logging utility class.

    This class provides static methods for logging messages at
    different levels. It is not meant to be instantiated, instead call
    its static methods directly.\n

    By default, it logs to console and to a file.\n

        Variables:
            MIN_LEVEL         (LEVEL): The minimum level the logger should log, default is DEBUG.
            FORMATTER     (Formatter): The formatter used to format the log message.
            WRITERS     list[Writer]): A list of writers to write to.
        
        Methods:
            d(message: str)
            i(message: str)
            s(message: str)
            w(message: str)
            e(message: str)
    """

    MIN_LEVEL: Level = Level.DEBUG
    """
    The minimum level, default is DEBUG.
    """

    FORMATTER: Formatter = Formatter()
    """
    The formatter used to format the log message.
    """

    WRITERS: dict[str, Writer] = {
        "console_writer": ConsoleWriter(),
        "file_writer": FileWriter()
    }
    """
    A list of writers to write to, by default, writes to console and to a file.\n
    If required, you can remove each writer by popping it with the keys console_writer and file_writer.
    """

    @staticmethod
    def __log(level: Level, message: str) -> None:
        """
        Main method that handles the core logic for logging.

            Parameters:
                level (Level): The logging level.
                message (str): The message to log.
        """
        if level < Log.MIN_LEVEL:
            return

        caller = get_caller()
        entry = LogEntry(level, caller, message)

        formatted_message = Log.FORMATTER.format(entry)
        for writer in Log.WRITERS.values():
            writer.write(formatted_message)


    @staticmethod
    def d(message: str) -> None:
        """
        Logs a debug message.
            
            Parameters:
                message (str): The message to log.
        """
        Log.__log(Level.DEBUG, message)


    @staticmethod
    def i(message: str) -> None:
        """
        Logs a info message.
            
            Parameters:
                message (str): The message to log.
        """
        Log.__log(Level.INFO, message)
    

    @staticmethod
    def s(message: str) -> None:
        """
        Logs a success message.
            
            Parameters:
                message (str): The message to log.
        """
        Log.__log(Level.SUCCESS, message)
    

    @staticmethod
    def w(message: str) -> None:
        """
        Logs a warning message.
            
            Parameters:
                message (str): The message to log.
        """
        Log.__log(Level.WARNING, message)
    

    @staticmethod
    def e(message: str) -> None:
        """
        Logs a error message.
            
            Parameters:
                message (str): The message to log.
        """
        Log.__log(Level.ERROR, message)
