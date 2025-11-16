import pytest

from src.decorators import log, my_function


def test_log_file():
    @log(filename="../mylog.txt")
    def my_function(x, y):
        return x + y

    my_function(2, 3)
    with open("../mylog.txt", encoding="utf-8") as f:
        line = f.readline()
        assert line == "\n"


@log(filename="../mylog.txt")
def add_numbers(a, b):
    return a + b


@log()
def test_my_function_consol(capsys):
    result = my_function(2, 3)
    captured = capsys.readouterr()
    assert result == 5
    assert "" in captured.out


def test_log_decor():
    @log()
    def my_function(x: int, y: int) -> int:
        return x + y

    assert my_function(1, 2) == 3
    assert my_function(2, 3) == 5
    assert my_function(4, 5) == 9


if __name__ == "__main__":
    pytest.main()
