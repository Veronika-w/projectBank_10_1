import pytest
import requests
from unittest.mock import patch
from src.external_api import convert_to_rub

@patch('requests.get')
def test_convert_to_rub(mock_get):
    transaction = {'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041', 'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'}
    amount = float(transaction.get("operationAmount", {}).get("amount", 0))
    currency = transaction.get("operationAmount", {}).get("currency", {}).get("code", {})
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
    mock_get.return_value.json.return_value = 2575114.472669
    assert convert_to_rub(mock_get) == 2575114.472669
    mock_get.assert_called_once_with(url)


@patch('requests.get')
def test_rub_convert_transaction(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 75.0}

    transaction = {
        "operationAmount": {
            "amount": "1",
            "currency": {"code": "USD"}
        }
    }

    result = convert_to_rub(transaction)
    assert result == 75.0