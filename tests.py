import pytest
from io import StringIO
from testfixtures import TempDirectory

from print_funcs import opening_statement


def test_print_functions(monkeypatch, capfd):
    test_string = "1"
    simulated_input = StringIO(test_string)
    monkeypatch.setattr('sys.stdin', simulated_input)
    out, err = capfd.readouterr()
    assert out == "1"


