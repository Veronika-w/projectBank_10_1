import pytest
from src.widget import mask_account_card, get_date

@pytest.fixture
def account_card():
    return "Visa Platinum 159683786870519"

def test_account_card(account_card):
    assert mask_account_card(account_card) == "Visa Platinum 1596 83** **** 5199"

@pytest.fixture
def date_time ():
    return "2024-03-11T02:26:18.671407"

def test_date_time(date_time):
    assert get_date (date_time) == "11.03.2024"