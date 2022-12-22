import pytest
from io import StringIO
from testfixtures import TempDirectory
import print_funcs
import util_functions
from print_funcs import opening_statement


def test_string_is_int(capfd):
    assert util_functions._string_is_int('104') is True
    assert util_functions._string_is_int('-35') is True
    assert util_functions._string_is_int(12537) is True
    assert util_functions._string_is_int(123.456) is True
    assert util_functions._string_is_int(2/3) is True
    assert util_functions._string_is_int('one') is False
    assert util_functions._string_is_int('Kratos') is False
    assert util_functions._string_is_int('') is False


def test_convert_string_to_numerical(capfd):
    assert util_functions.convert_string_to_numerical('12.0') == 12
    assert util_functions.convert_string_to_numerical('0.001') == 0.001
    assert util_functions.convert_string_to_numerical('Atreus') is None


def test_string_is_float(capfd):
    assert util_functions._string_is_float('12.0') is True
    assert util_functions._string_is_float('12') is True
    assert util_functions._string_is_float('0') is True
    assert util_functions._string_is_float('-0.123') is True
    assert util_functions._string_is_float('-0') is True
    assert util_functions._string_is_float('Do not trust Odin') is False
    assert util_functions._string_is_float('12.12.134.233') is False
    assert util_functions._string_is_float('5/2') is False
    assert util_functions._string_is_float('apple.cider.is.good') is False
    assert util_functions._string_is_float('(12/2)/2') is False

