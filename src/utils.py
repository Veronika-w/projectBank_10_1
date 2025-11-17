import json
from typing import Any
import logging


logger = logging.getLogger('utils')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('C:/Users/i3/my_pj/pythonBank//logs/utils.log', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


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
