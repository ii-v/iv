#!/usr/bin/env python3
from roman_numerals import *

def test_convert():
    assert convert(3) == "III"
    assert convert("III") == 3
