import json
import logging
import os
from typing import Any

logger = logging.getLogger("utils")
logger.setLevel(logging.INFO)
log_dir = os.path.join(os.path.dirname(__file__), "../logs")
log_file = os.path.join(log_dir, "utils.log")
file_handler = logging.FileHandler(log_file, encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def read_json_operation(json_path: str) -> Any:
    """Функция, возвращает список словарей с данными о финансовых транзакциях"""
    try:
        if not os.path.exists(json_path):
            logger.error(f"Файл {json_path} не найден")
            return []

        logger.debug(f"Попытка загрузить файл: {json_path}")

        with open(json_path, "r", encoding="utf-8") as file:
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


#
#
# if __name__ == "__main__":
#     print(read_json_operation("../data/operations.json"))
