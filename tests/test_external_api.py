import os
from unittest.mock import patch

from src.external_api import convert_to_rub

API_KEY = os.getenv("API_KEY")


@patch("requests.request")
def test_convert_to_rub(mock_get):
    transaction = {
        "id": 782295999,
        "state": "EXECUTED",
        "date": "2019-09-11T17:30:34.445824",
        "operationAmount": {"amount": "54280.01", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 24763316288121894080",
        "to": "Счет 96291777776753236930",
    }
    mock_get.return_value.status_code = 200
    amount = float(transaction.get("operationAmount", {}).get("amount", 0))
    currency = transaction.get("operationAmount", {}).get("currency", {}).get("code", {})
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
    mock_get.return_value.json.return_value = {"result": 4369103.090999}
    assert convert_to_rub(transaction) == 4369103.090999
    mock_get.assert_called_once_with("GET", url, headers={"apikey": API_KEY})


@patch("requests.get")
def test_rub_convert_transaction(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 75.0}

    transaction = {"operationAmount": {"amount": "1", "currency": {"code": "USD"}}}

    result = convert_to_rub(transaction)
    assert result == 80.491936
