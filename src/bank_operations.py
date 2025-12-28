import re
from collections import Counter

from src.read_csv_excel import read_transactions_excel

operations = [
    {
        "id": 214024827,
        "state": "EXECUTED",
        "date": "2018-12-20T16:43:26.929246",
        "operationAmount": {"amount": "70946.18", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 10848359769870775355",
        "to": "Счет 21969751544412966366",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 587085106,
        "state": "EXECUTED",
        "date": "2018-03-23T10:45:06.972075",
        "operationAmount": {"amount": "48223.05", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Открытие вклада",
        "to": "Счет 41421565395219882431",
    },
    {
        "id": 522357576,
        "state": "EXECUTED",
        "date": "2019-07-12T20:41:47.882230",
        "operationAmount": {"amount": "51463.70", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 48894435694657014368",
        "to": "Счет 38976430693692818358",
    },
]

operations2 = ("Открытие вклада", "Перевод организации")

data_xl = read_transactions_excel("../data/transactions_excel.xlsx")


def process_bank_search(operations_list: list[dict], keyword: str) -> list[dict]:
    """Функция, которая будет принимать список словарей с данными
    о банковских операциях и строку поиска, а возвращать список словарей,
    у которых в описании есть данная строка"""
    chosen_operations = []
    for operation in operations_list:
        description = operation.get("description", "")
        if isinstance(description, str) and re.search(keyword, description, re.IGNORECASE):
            chosen_operations.append(operation)
    return chosen_operations


# if __name__ == "__main__":
#     print(process_bank_search(data_xl,"Открытие"))


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """Функция, которая будет принимать список словарей с данными о банковских операциях и список категорий операций,
    а возвращать словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории"""
    categories_counter = Counter()
    for operation in data:
        description = operation.get("description", "")
        for category in categories:
            if category.lower() in description.lower():
                categories_counter[category] += 1
    return categories_counter


# print(process_bank_operations(operations, operations2))
