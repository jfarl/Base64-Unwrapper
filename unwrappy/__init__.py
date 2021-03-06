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
    S = s if version_info.major != 3 else s.decode("utf-8")
    return S.strip().strip("\n")


def unwrap_strings(strings=[], debug=False):
    """
    Unwrapper function
    Takes in list of strings
    Unwraps them all sequentially
    """
    unwrapped = list()
    if debug:
        print("Length of input: {0}".format(len(strings)))
        print("Starting unwrap")
    for s in strings:
        try:
            unwrapped.append([s, unwrap_complete(s, debug)])
        except Exception as e:
            print("ERROR: {0}".format(e))
    return unwrapped 

def unwrap_complete(string, debug=False):
    """
    Unwrap until it can't be unwrapped anymore!
    """
    counter = 0
    unwrapped = False
    if debug:
        print("Unwrap loop started on string {0}".format(string))
    try:
        while DS(prep_string(string)):
            counter += 1
            string = DS(prep_string(string))
            if debug:
                print("Cycle {0} -> {1}".format(counter, string))
    except:
        if counter == 0:
            raise ValueError("String is not Base64 encoded!")
    return string


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
    try:
        print_unwrapped(unwrap_strings(args.strings, args.d), args.d)
    except Exception as e:
        print("Error: {0}".format(e))

# end
