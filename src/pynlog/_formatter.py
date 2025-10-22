from datetime import datetime


from pynlog._level import Level
from pynlog._logentry import LogEntry


class Formatter:
    """
    Used to format log entries into strings.\n
    Handles alignment, color codes, and timestamp insertion.\n
        Variables:
            DEBUG   (str): Used to prefix the level tag for DEBUG level logs.
            INFO    (str): Used to prefix the level tag for INFO level logs.
            SUCCESS (str): Used to prefix the level tag for SUCCESS level logs.
            WARNING (str): Used to prefix the level tag for WARNING level logs.
            ERROR   (str): Used to prefix the level tag for ERROR level logs.
            END     (str): Used to suffix the level tag.


        Methods:
            format(entry: LogEntry)
    """

    DEBUG: str = "\033[35m"
    """
    Color for DEBUG level logs.
    """

    INFO: str = "\033[36m"
    """
    Color for INFO level logs.
    """

    SUCCESS: str = "\033[32m"
    """
    Color for SUCCESS level logs.
    """
    
    WARNING: str = "\033[33m"
    """
    Color for WARNING level logs.
    """
    
    ERROR: str = "\033[31m"
    """
    Color for ERROR level logs.
    """
    
    END: str = "\033[0m"
    """
    Used to reset colors.
    """

    @property
    def __COLORS(self) -> dict[Level, str]:
        return {
            Level.DEBUG: self.DEBUG,
            Level.INFO: self.INFO,
            Level.SUCCESS: self.SUCCESS,
            Level.WARNING: self.WARNING,
            Level.ERROR: self.ERROR,
        }
    

    def __get_color(self, level: Level) -> str:
        """
        Returns a color string depending on the `level`.

            Parameters:
                level (Level): The log level.
            
            Returns:
                str: A color string.
        """
        if level in self.__COLORS:
            return self.__COLORS[level]
        return self.END


    def format_time(self, time: datetime) -> str:
        """
        Returns a string representing the passed datetime.
            Example Output:
                2025-10-22 18:05:01.123

            Parameters:
                time (datetime): A datetime object
            
            Returns:
                str: A datetime as a string
        """
        return time.strftime("%Y-%m-%d %H:%M:%S.") + f"{int(time.microsecond / 1000):03d}"


    def format(self, entry: LogEntry) -> str:
        """
        Formats a LogEntry.

            Parameters:
                entry (LogEntry): A dataclass containing information needed to create the string.

            Returns:
                str: A formatted strings
        """
        time_str = self.format_time(entry.time)
        tag_str = f"[{entry.level}]"
        return f"[{time_str}] {self.__get_color(entry.level)}{tag_str:<10}{self.END} {entry.caller}: {entry.message}"