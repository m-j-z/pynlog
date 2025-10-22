from os import makedirs, path
from datetime import datetime


from pynlog._writer import Writer


class FileWriter(Writer):
    """
    A helper class used by Log to write to a file.

        Parameters:
            output_path (str): The path to output log files at.

        Variables:
            MAX_SIZE    (int): The maximum size of a file before writing to a new file.
            EXT         (str): The extension used for each log file.
        
        Methods:
            create_file_name()
            write(message: str)
    """

    MAX_SIZE: int = 50 * 1024 * 1024
    """
    The maximum size before the writer will write to a new file, default is 50mb.
    """

    EXT: str = ".log"
    """
    The extension used for each log file.
    """

    def __init__(self, output_path: str = "logs") -> None:
        makedirs(output_path, exist_ok=True)
        self.__output_path = output_path
        self.__prev_filename = ""
        self.__file_prefix = ""
        self.__count = 0

    
    def create_file_name(self, now: datetime):
        """
        Creates a filename from the current datetime.

            Returns:
                str: A filename.
        """
        time_str = now.strftime("%Y-%m-%d_%H-%M-%S")
        file_name = f"log_{time_str}"

        if self.__file_prefix == file_name:
            self.__count += 1
            return f"log_{time_str}_{self.__count + 1}{self.EXT}"
        
        self.__file_prefix = file_name
        self.__count = 0
        return f"log_{time_str}{self.EXT}"
            


    def write(self, message: str):
        """
        Writes a message to a file.

            Parameters:
                message (str): The message to write.
        """

        if not self.__prev_filename or (path.exists(self.__prev_filename) and path.getsize(self.__prev_filename) >= self.MAX_SIZE):
            self.__prev_filename = self.__output_path + "/" + self.create_file_name(datetime.now())
        
        with open(self.__prev_filename, "a") as file:
            file.write(message + "\n")
