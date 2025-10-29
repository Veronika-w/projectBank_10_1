import pytest

from src.decorators import log, my_function


@log(filename="../mylog.txt")
def test_my_function(capsys):
    result = my_function(1, 2)
    captured = capsys.readouterr()
    assert result == 3
    assert "Функция my_function" in captured.out
