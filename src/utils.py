import json
from typing import Any


def read_json_operation(path: str) -> Any:
    """Функция, возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
            if not isinstance(data, list):
                return []
            return data
    except FileNotFoundError:
        print("Файл не найден")
        return []
    except json.JSONDecodeError:
        print("Ошибка декодирования файла")
        return []


if __name__ == "__main__":
    print(read_json_operation("C:/Users/i3/my_pj/pythonBank/data/operations.json"))
