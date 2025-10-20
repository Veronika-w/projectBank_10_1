import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "type_num, result_account_card",
    [
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
    ],
)
def test_get_mask_card_number(type_num, result_account_card):
    assert mask_account_card(type_num) == result_account_card


@pytest.fixture
def date_time():
    return "2024-03-11T02:26:18.671407"


def test_date_time(date_time):
    assert get_date(date_time) == "11.03.2024"
