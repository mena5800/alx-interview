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
    n_bits = 0
    for num in data:
        if (num >> 7) > 1:
            return False
        if n_bits > 0:
            # check the msb is 1 and 7th bit is 0
            if ((num >> 7) and ((num >> 6) & 1) == 0):
                n_bits -= 1
            else:
                return False
        elif num <= 127:
            continue
        else:
            i = 6
            while ((num >> i) & 1):
                n_bits += 1
                i -= 1
            if n_bits == 0:
                return False
    return True if n_bits == 0 else False
