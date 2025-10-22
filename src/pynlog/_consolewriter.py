from pynlog._writer import Writer


class ConsoleWriter(Writer):
    """
    A helper class used by Log to write to the console.

        Methods:
            write(message: str)
    """
    
    def write(self, message: str) -> None:
        """
        Writes a message to the console.

            Parameters:
                message (str): The message to write.
        """
        print(message)
