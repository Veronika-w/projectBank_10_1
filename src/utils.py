import json


def get_avg_for_operation(path: str) -> list[str]:
    """Функция, возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(path, encoding='utf-8') as f:
            operation_data = json.load(f)
            return operation_data
    except FileNotFoundError:
        print("Невозможно открыть файл")
        return []


if __name__ == '__main__':
    get_avg_for_operation('../data/operations.json')

print(get_avg_for_operation('../data/operations.json'))


