from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(type_and_number: str) -> str:
    """Функция маскировки типа и номер карты или счет"""

    type_number = type_and_number.lower()
    if "счет" in type_number:
        number_account = type_and_number[-6:]
        masked_account = get_mask_account(number_account)
        return f"Счет {masked_account}"
    else:
        number_card = type_and_number[-16:]
        masked_card = get_mask_card_number(number_card)
        type_card = type_and_number[:-16]
    return f"{type_card} {masked_card}"


if __name__ == "__main__":
    print(mask_account_card("MasterCard 7158300734726758"))

    print(mask_account_card("Счет 73654108430135874305"))


def get_date(format_data: str) -> str:
    """Функция возврата даты в формате 'ДД.ММ.ГГГГ'"""
    new_format = format_data[8:10] + "." + format_data[5:7] + "." + format_data[0:4]
    return new_format


print(get_date("2024-03-11T02:26:18.671407"))
