# import pytest
#
# from src.bank_operations import process_bank_search, process_bank_operations
#
#
# @pytest.fixture()
# def operations():
#     result = [{"description": "Перевод организации"},
#             {"description": "Открытие вклада"},
#             {"description": "Перевод организации"}]
#     return result
#
#
# def test_process_bank_search(operations):
#     result = process_bank_search(operations, "перевод")
#     expected = [{"description": "Перевод организации"}]
#     assert result == expected
#
#
# def test_process_bank_search_2():
#     result = process_bank_search("открытие")
#     expected = [{"description": "Открытие вклада"}]
#     assert result == expected
#
# def test_process_bank_operations():
#     assert process_bank_operations(["Перевод организации"]) == {"Перевод организации": 2}