from pynlog._formatter import Formatter
from pynlog._writer import Writer
from pynlog._consolewriter import ConsoleWriter
from pynlog._filewriter import FileWriter
from pynlog._level import Level
from pynlog._utility import get_caller
from pynlog._logentry import LogEntry

class Log:
    MIN_LEVEL: Level = Level.DEBUG
    FORMATTER: Formatter = Formatter()
    WRITERS: list[Writer] = [ConsoleWriter(), FileWriter()]

    @staticmethod
    def __log(level: Level, message: str):
        if level < Log.MIN_LEVEL:
            return

        caller = get_caller()
        entry = LogEntry(level, caller, message)

        formatted_message = Log.FORMATTER.format(entry)
        for writer in Log.WRITERS:
            writer.write(formatted_message)


    @staticmethod
    def d(message: str):
        Log.__log(Level.DEBUG, message)


    @staticmethod
    def i(message: str):
        Log.__log(Level.INFO, message)
    

    @staticmethod
    def s(message: str):
        Log.__log(Level.SUCCESS, message)
    

    @staticmethod
    def w(message: str):
        Log.__log(Level.WARNING, message)
    

    @staticmethod
    def e(message: str):
        Log.__log(Level.ERROR, message)
