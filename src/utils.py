import json
from typing import Any
import logging
import os


logger = logging.getLogger('utils')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('C:/Users/i3/my_pj/pythonBank/logs/utils.log', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def read_json_operation(path: str) -> Any:
    """Функция, возвращает список словарей с данными о финансовых транзакциях"""
    try:
        if not os.path.exists(path):
            logger.error(f"Файл {path} не найден")
            return []

        logger.debug(f"Попытка загрузить файл: {path}")

        with open(path, "r", encoding="utf-8") as file:
            try:
                data = json.load(file)
                logger.debug("Данные успешно загружены из файла")

                if not isinstance(data, list):
                    logger.error("Данные в файле не являются списком")
                    return []
                logger.info("Данные успешно проверены и корректны")
                return data

            except json.JSONDecodeError:
                logger.error("Ошибка декодирования JSON")
                return []
    except Exception:
        logger.exception("Критическая ошибка при работе с файлом")
    return []


if __name__ == "__main__":
    print(read_json_operation("C:/Users/i3/my_pj/pythonBank/data/operations.json"))
