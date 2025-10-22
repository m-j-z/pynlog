from inspect import currentframe


def truncate(string: str, max_len: int = 24) -> str:
    """
    Truncates a `string` to exactly `max_length` characters.

        Example Output:
            ...a_name

        Parameters:
            string (str): The string to truncate.
            max_len (int): The maximum length of a string before truncation happens, default is 24.
        
        Returns:
            str: The truncated string.
    """
    if (len(string) <= max_len):
        return string.ljust(max_len)
    return "..." + string[-(max_len - 3):]


def get_caller(n: int = 3) -> str:
    """
    Returns the caller's function name and potentially class name.

        Example Output:
            myclass.myfunction

        Parameters:
            n (int): The number of frames to go back.
        
        Returns:
            str: The caller as a string.
    """
    frame = currentframe()
    for _ in range(n):
        if not frame:
            return ""
        frame = frame.f_back
    
    if not frame or not frame.f_code:
        return ""
    
    func_name = frame.f_code.co_name    
    cls_name = None
    if "self" in frame.f_locals:
        cls_name = frame.f_locals["self"].__class__.__name__
    elif "cls" in frame.f_locals:
        cls_name = frame.f_locals["cls"].__name__
    
    if cls_name:
        return truncate(f"{cls_name}.{func_name}")
    return truncate(func_name)
