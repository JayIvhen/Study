""" Adeptus Mechanicus Portable Translator

Program for translating bynary speach of martians.

"""

# Nothing to comment.

__author__ = "JayIvhen"

# stdlib import section
import os

# third party import section

# local import section
import bynary_to_string

def main():
    """ main

    Read string from input, translate them and return.

    """
    while True:
        str_ = input()
        if str_ == 'exit':
            break
        try:
            if set(str_) != set(("01 ")):
                print(bynary_to_string.str_to_byn(str_))
                print(os.times())
            else:
                print(bynary_to_string.byn_to_utf(str_))
                print(os.times())
        except:
            print("Wrong input")

main()