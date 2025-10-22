from pynlog._writer import Writer


class ConsoleWriter(Writer):
    def write(self, message: str):
        """
        Writes a message to the console.

            Parameters:
                message (str): The message to write.
        """
        print(message)
