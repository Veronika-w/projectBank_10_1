import pytest

from src.decorators import my_function, log


@log(filename="../mylog.txt")
def test_my_function(capsys):
    result = my_function(1, 2)
    captured = capsys.readouterr()
    assert result == 3
    assert "Функция my_function" in captured.out

