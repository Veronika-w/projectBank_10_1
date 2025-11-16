import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")


def convert_to_rub(transaction: dict) -> float:
    """Функция осуществляет конвертацию суммы транзакции в рубли"""
    try:
        amount = transaction["operationAmount"]["amount"]

        currency = transaction["operationAmount"]["currency"]["code"]
        currency_rub = "RUB"

        if currency != "RUB":
            url = f"https://api.apilayer.com/exchangerates_data/convert?to={currency_rub}&from={currency}&amount={amount}"
            headers = {"apikey": API_KEY}
            response = requests.get("GET", url, headers=headers)
            status_code = response.status_code
            result = response.json()
            if status_code == 200:
                return result["result"]
            else:
                return f"Запрос не выполнен.\nКод ошибки: {status_code}.\nОписание ошибки: {result}."
        else:
            return amount
    except Exception as e:
                print(f"Ошибка конвертации: {e}")


print(
    convert_to_rub(
        {
            "id": 649467725,
            "state": "EXECUTED",
            "date": "2018-04-14T19:35:28.978265",
            "operationAmount": {"amount": "96995.73", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Счет 27248529432547658655",
            "to": "Счет 97584898735659638967",
        },
    )
)

print(
    convert_to_rub(
        {
            "id": 782295999,
            "state": "EXECUTED",
            "date": "2019-09-11T17:30:34.445824",
            "operationAmount": {"amount": "54280.01", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 24763316288121894080",
            "to": "Счет 96291777776753236930",
        }
    )
)
