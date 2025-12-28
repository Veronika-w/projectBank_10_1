from src.bank_operations import process_bank_operations, process_bank_search


def test_process_bank_search_match() -> None:
    transactions = [
        {"description": "Покупка продуктов"},
        {"description": "Оплата услуг"},
        {"description": "Перевод организации"},
        {"description": "Открытие вклада"},
    ]
    search_string = "Перевод организации"
    assert process_bank_search(transactions, search_string) == [{"description": "Перевод организации"}]

def test_process_bank_operations() -> None:
    assert process_bank_operations([], []) == {}
    assert process_bank_operations([], ["Перевод организации", "Открытие вклада",
                                        "Перевод с карты на счет", "Перевод с карты на карту"]) == {}




