import json


def read_json_operation(path: str) -> list[dict]:
    """Функция, возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(path, encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                return []
    except FileNotFoundError:
        return []
    return data


if __name__ == "__main__":
    print(read_json_operation("../data/operations.json"))
