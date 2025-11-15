import json


def read_json_operation(path: str) -> list[dict]:
    """Функция, возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        print ("Файл не найден")
        return []
    except json.JSONDecodeError:
        print("Ошибка декодирования файла")
        return []


if __name__ == "__main__":
    print(read_json_operation("C:/Users/i3/my_pj/pythonBank/data/operations.json"))
