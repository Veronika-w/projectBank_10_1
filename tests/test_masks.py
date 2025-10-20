import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_num, result_card",
    [
        ("1234567890123456", "1234 56** **** 3456"),
        ("1234561111783456", "1234 56** **** 3456"),
        ("1234567890127890", "1234 56** **** 7890"),
    ],
)
def test_get_mask_card_number(card_num, result_card):
    assert get_mask_card_number(card_num) == result_card


@pytest.mark.parametrize(
    "acc_number, expected", [("12345678", "**5678"), ("123456", "**3456"), ("123456789", "**6789")]
)
def test_get_mask_account(acc_number, expected):
    assert get_mask_account(acc_number) == expected
