#!/usr/bin/env python3
import roman_numerals

def test_input_is_arabic():
    assert roman_numerals.input_is_integer(3) == True
    assert roman_numerals.input_is_integer("III") == False
