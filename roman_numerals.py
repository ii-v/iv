#!/usr/bin/env python3
# Copyright 2016 <iiv@openmailbox.org>
# License: MIT

def roman_number_is_valid(n):
    """roman_number_is_valid(n) -> Boolean""" # TODO
    pass

roman_numbers = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, 
                 "C" : 100, "D" : 500, "M" : 1000}

def convert(n):
    """convert(n) -> Integer""" # TODO
    try:
        for character in n:
            if character in roman_numbers:
                return "Roman"
    except:    
        return "Arabic"
