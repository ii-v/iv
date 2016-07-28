#!/usr/bin/env python3
import roman_numerals

def test_convert():
    assert roman_numerals.convert(3) == "III"
    assert roman_numerals.convert("III") == 3
