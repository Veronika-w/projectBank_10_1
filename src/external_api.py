import os
import requests
from dotenv import load_dotenv
import json

load_dotenv()

API_KEY = os.getenv("API_KEY")

def convert_to_rub(transaction: dict) -> float:
    """Функция осуществляет конвертацию суммы транзакции в рубли"""
    currency_to = "RUB"
    currency_from = transaction.get('operationAmount', {}).get('currency', {}).get('code', {})
    amount = float(transaction.get('operationAmount', {}).get('amount', 0))
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={currency_to}&from={currency_from}&amount={amount}"
    payload = {}
    headers = {
        "apikey": f"{API_KEY}"
    }
    if currency_from == "RUB":
        return amount
    elif currency_from == {}:
        return amount
    else:
        response = requests.get ( f"https://api.apilayer.com/exchangerates_data/convert?to={currency_to}&from={currency_from}&amount={amount}")
        response = requests.request("GET", url, headers=headers, data=payload)
        status_code = response.status_code
        result = response.text
        print(currency_from)
        print(amount)
        print(response.status_code)
        if status_code == 200:
            python_response = json.loads(result)
            amount = float(python_response.get('result', 0))
            return amount


print(convert_to_rub({"id": 596171168,
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
  } ))

print(convert_to_rub({
    "id": 863064926,
    "state": "EXECUTED",
    "date": "2019-12-08T22:46:21.935582",
    "operationAmount": {
      "amount": "41096.24",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 90424923579946435907"
  }))