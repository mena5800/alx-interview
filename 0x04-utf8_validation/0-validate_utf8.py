#!/usr/bin/python3
"""this file contain a method that determines if a given
data set represents a valid UTF-8 encoding."""


def validUTF8(data):
    """
    method that determines if a given data set
    represents a valid UTF-8 encoding or not.

    Args:
      data : list of integers,
            each integer represents byte encoding in utf-8.
    Return:
      bool : True if valid utf otherwise False.

    """
    n_bytes = 0
    
    for num in data:
        if n_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            if (num >> 5) == 0b110:
                n_bytes = 1
            elif (num >> 4) == 0b1110:
                n_bytes = 2
            elif (num >> 3) == 0b11110:
                n_bytes = 3
            elif (num >> 7):
                return False  # 10xxxxxx or 11111xxx are invalid starting bytes
        else:
            # Check that the byte follows the pattern 10xxxxxx
            if (num >> 6) != 0b10:
                return False
            n_bytes -= 1

    return n_bytes == 0
