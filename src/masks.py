import logging

logger = logging.getLogger("masks")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("../logs/masks.log", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Функцию маскировки номера банковской карты в формате XXXX XX** **** XXXX"""
    try:
        card_str = str(card_number)
        logger.warning("Номер карты должен содержать 16 цифр")
        if len(card_str) != 16:
            raise ValueError("Номер карты должен содержать 16 цифр")
        format_card = card_str[:4] + " " + card_str[4:6] + "**" + " " + "****" + " " + card_str[-4:]
        logger.info("Маскировка номера банковской карты")
        return format_card
    except Exception as ex:
        logger.error(f"Произошла ошибка: {ex}")


print(get_mask_card_number("7000792289606361"))
print(get_mask_card_number("700079228960636"))


def get_mask_account(account_number: str) -> str:
    """Маскирует номер счета по шаблону **XXXX"""
    try:
        account_str = str(account_number)
        logger.warning("Номер счета должен содержать минимум 6 цифр")
        if len(account_str) < 6:
            raise ValueError("Номер счета должен содержать минимум 6 цифр")

        format_account = "**" + account_str[-4:]
        logger.info("Маскировка номера счета")
        return format_account
    except Exception as ex:
        logger.error(f"Произошла ошибка: {ex}")


print(get_mask_account("736541084301358714305"))
print(get_mask_account("85305"))
