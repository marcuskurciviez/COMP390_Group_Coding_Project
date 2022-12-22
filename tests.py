import pytest
from io import StringIO
from testfixtures import TempDirectory

from print_funcs import opening_statement


def test_print_functions(monkeypatch, capfd):
    monkeypatch.setattr('builtins.input', lambda _: '1')
    i = input(opening_statement())
    assert i == '1'


