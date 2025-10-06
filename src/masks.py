def get_mask_card_number(card_number: str) -> str:
    """Функцию маскировки номера банковской карты в формате XXXX XX** **** XXXX"""
    card_str = str(card_number)
    if len(card_str) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр")
    format_card = card_str[:4] + " " + card_str[4:6] + "**" + " " + "****" + " " + card_str[-4:]

    return format_card


print(get_mask_card_number("7000792289606361"))


def get_mask_account(account_number: str) -> str:
    """Маскирует номер счета по шаблону **XXXX"""
    account_str = str(account_number)

    if len(account_str) < 6:
        raise ValueError("Номер счета должен содержать минимум 6 цифр")

    format_account = "**" + account_str[-4:]

    return f"Счет {format_account}"


print(get_mask_account("73654108430135874305"))
