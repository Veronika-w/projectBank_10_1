import pytest

from src.bank_operations import process_bank_operations, process_bank_search

# @pytest.fixture()
# def operations():
#     result = [{"description": "Перевод организации"},
#             {"description": "Перевод с карты на карту"},
#             {"description": "Открытие вклада"}]
#     return result
#
#
# def test_process_bank_search(operations):
#     result = process_bank_search("открытие")
#     expected = [{"description": "Открытие вклада"}]
#     assert result == expected
#
# def test_process_bank_operations():
#     assert process_bank_operations(operations, ["Перевод организации"]) == {"Перевод организации": 2}


def test_process_bank_search_match() -> None:
    transactions = [
        {"description": "Покупка продуктов"},
        {"description": "Оплата услуг"},
        {"description": "Перевод организации"},
        {"description": "Открытие вклада"},
    ]
    search_string = "Перевод организации"
    assert process_bank_search(transactions, search_string) == [{"description": "Перевод организации"}]
