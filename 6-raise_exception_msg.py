def raise_exception_msg(message=""):
    """
    Raises a NameError exception with a custom message.

    Args:
    message (str): The message to be included with the exception.
    """
    raise NameError(message)

# Test case
try:
    raise_exception_msg("C is fun")
except NameError as ne:
    print(ne)
