from typing import Any
from unittest import mock
import os


from src.read_csv_excel import read_transactions_csv, read_transactions_excel


@mock.patch("pandas.read_csv", side_effect=FileNotFoundError)
def test_file_not_csv(mock_open: Any) -> None:
    result = read_transactions_csv("transactions.csv")
    assert result == []


@mock.patch("pandas.read_excel", side_effect=FileNotFoundError)
def test_file_not_excel(mock_open: Any) -> None:
    result = read_transactions_excel("transactions_excel.csv")
    assert result == []


def test_read_transactions_csv_not_file():
    file1_path = os.path.join("data", "transactions0.csv")
    assert read_transactions_csv(file1_path) == []


def test_read_transactions_excel_not_file():
    file1_path = os.path.join("data", "transactions_excel0.xlsx")
    assert read_transactions_excel(file1_path) == []