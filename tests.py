import pytest
from io import StringIO
from testfixtures import TempDirectory

import print_funcs
from print_funcs import opening_statement


def test_opening_statement(monkeypatch, capfd):
    test_string = ""
    simulated_input = StringIO(test_string)
    monkeypatch.setattr('sys.stdin', simulated_input)
    assert print_funcs.opening_statement() is None
    out, err = capfd.readouterr()
    assert out == "1"


