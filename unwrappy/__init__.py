#!/usr/bin/env python
#-*- coding: utf-8 -*-

from base64 import decodestring as DS
from argparse import ArgumentParser

"""
Unwrappy library
Has a few functions
"""

from sys import version_info

def prep_string(s):
    """
    Due to Python2/3 differences string conversion is different
    """
    return bytes(s) if version_info.major != 3 else bytes(s, "utf-8")


def clean_string(s):
    """
    Same reasoning as prep_string
    """
    S =  s if version_info.major != 3 else s.decode("utf-8")
    return S.strip().strip("\n")


def unwrap_strings(strings=[], debug=False):
    """
    Unwrapper function
    Takes in list of strings
    Unwraps them all sequentially
    """
    unwrapped = list()
    for s in strings:
        try:
            unwrapped.append([s, DS(prep_string(s))])
        except Exception as e:
            print("ERROR: {0}".format(e))
    return unwrapped 


def print_unwrapped(pairs=[], debug=False):
    """
    Print the unwrapped strings by accepting a list of pairs
    """
    for i, p in enumerate(pairs):
        print("{0}: {1} -> {2}".format(i+1, p[0], clean_string(p[1])))
    return True


def main(*args, **kwargs):
    """
    Main function
    Add argument parser and throw args passed into the unwrapper
    """
    ap = ArgumentParser(description="Unwrap some Base64 strings")
    ap.add_argument("strings", metavar="S", type=str, nargs="+",
            help="Strings to unwrap")
    ap.add_argument("-d", action="store_const", default=False, const=True)

    args = ap.parse_args()
    print_unwrapped(unwrap_strings(args.strings, args.d))

# end
