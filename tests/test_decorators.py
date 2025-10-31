import pytest

from src.decorators import log, my_function


def test_log_file():
    @log(filename="../mylog.txt")
    def my_function(x, y):
        return x + y

    my_function(2, 3)
    with open("../mylog.txt", encoding="utf-8") as f:
        line = f.readline()
        assert line == f"Функция: my_function\n"


@log()
def test_my_function(capsys):
    result = my_function(2, 3)
    captured = capsys.readouterr()
    assert result == 5
    assert "" in captured.out


def test_log(capsys):
    @log()
    def my_function(x, y):
        return x + y

    my_function(2, 3)
    result = capsys.readouterr()
    assert result.out == "Функция: my_function\n"


if __name__ == "__main__":
    pytest.main()
