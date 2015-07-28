#!/usr/bin/env python
#-*- coding: utf-8 -*-

# Run this module with nosetests at the root of the project tree
# This is not meant to run on it's own

from unwrappy import *
from base64 import encodestring as ES

teststrings = [
        "Steve", "Jon", "Ben", "Eric", "Python",
        "Apple", "Bear", "Banana", "Cookie",
        "123456789Zero", "90210",
        "Racket is better", "Don't use Ruby",
        "Why am I writing all of these",
        "Oh right it's a unit test",
    ]


def test_bunch_of_strings():
    """
    Test a whole bunch of strings
    See if they encode and decode properly
    """
    byte_strings = [clean_string(ES(prep_string(s))) for s in teststrings]
    for x in byte_strings:
        print(x)

    my_pairs = unwrap_strings(byte_strings)
    
    # Now test if the unwrapped match their originals
    for i, p in enumerate(my_pairs):
        assert teststrings[i] == clean_string(p[1])

# end
