""" bynary_to_str

Functions for bin code to UTF and revers

"""

# BinaryToString
# For adeptus mechanikum Order

__author__ = "JayIvhen"
__all__ = ['str_to_byn', 'byn_to_utf']

# StdLib import section.

# Third party import section.

# Local import section.


def str_to_byn(str_):
    """ str_to_bin([string]) UTF-8

    Takes string. Return string of binary bites splited with " "
    Example
    input: bynary_to_string.str_to_byn('ex')
    output: '1100101 1111000'

    """

    return ' '.join(bin(byte).lstrip('0b') for Item in str_ for byte in Item.encode())


def byn_to_utf(str_):
    """ bin_to_utf(string) string may contain only '1','0',' '.

    Takes binary bites. Return UTF decoded str.
    Example
    input: byn_to_utf('1100101 1111000')
    output: 'ex'

    """

    byte = bytearray()
    for item in str_.split(' '):
        byte.append(int(item, 2))
    return byte.decode()




