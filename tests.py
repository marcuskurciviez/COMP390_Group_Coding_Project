import pytest
import util_functions


def test_string_is_float(capfd):
    assert util_functions._string_is_float('12') is True
    assert util_functions._string_is_float('12.1234') is True
    assert util_functions._string_is_float('-0.12') is True
    assert util_functions._string_is_float('12.3124.1343.1563') is False
    assert util_functions._string_is_float('Apple') is False
    assert util_functions._string_is_float('(12/3)/2') is False
    assert util_functions._string_is_float('120/7') is False


def test_convert_string_to_numerical(capfd):
    assert util_functions.convert_string_to_numerical('12.0') == 12
    assert util_functions.convert_string_to_numerical('-0.143') == -0.143
    assert util_functions.convert_string_to_numerical('0.0') == 0
    assert util_functions.convert_string_to_numerical('john') is None


def test_string_is_int(capfd):
    assert util_functions._string_is_int('104.7') is False
    assert util_functions._string_is_int('-35') is True
    assert util_functions._string_is_int(-35) is True
    assert util_functions._string_is_int(4.6) is True
    assert util_functions._string_is_int(True) is True
    assert util_functions._string_is_int(Exception) is False
    assert util_functions._string_is_int(2/3) is True

