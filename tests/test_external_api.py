import pytest
import requests
from unittest.mock import patch
from src.external_api import convert_to_rub
from unittest.mock import Mock
from src.utils import read_json_operation
import os


@patch('requests.get')
def test_convert_to_rub(mock_get):
    transaction = {"id": 596171168,
    "state": "EXECUTED",
    "date": "2018-07-11T02:26:18.671407",
    "operationAmount": {
      "amount": "79931.03",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 72082042523231456215"
  }

    amount = float(transaction.get("operationAmount", {}).get("amount", 0))
    currency = transaction.get("operationAmount", {}).get("currency", {}).get("code", {})
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
    mock_get.return_value.json.return_value = 79931.03
    assert convert_to_rub(mock_get) == 79931.03
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



