import re


my_transactions = [{
    "id": 214024827,
    "state": "EXECUTED",
    "date": "2018-12-20T16:43:26.929246",
    "operationAmount": {
      "amount": "70946.18",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Счет 10848359769870775355",
    "to": "Счет 21969751544412966366"
  },
  {
    "id": 522357576,
    "state": "EXECUTED",
    "date": "2019-07-12T20:41:47.882230",
    "operationAmount": {
      "amount": "51463.70",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Счет 48894435694657014368",
    "to": "Счет 38976430693692818358"
  },
  {
    "id": 895315941,
    "state": "EXECUTED",
    "date": "2018-08-19T04:27:37.904916",
    "operationAmount": {
      "amount": "56883.54",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод с карты на карту",
    "from": "Visa Classic 6831982476737658",
    "to": "Visa Platinum 8990922113665229"
  }]




def process_bank_search(user_date: str) -> str:
    """Соединяем день, месяц и год в дату"""
    times = user_date[:user_date.find("T")].split("-")
    reversed_times = times[::-1]
    if len(times) < 2:
        return 'Ошибка ввода данных'
    else:
        return ".".join(reversed_times)



def process_bank_operations(transactions: dict) -> str:
    for transaction in transactions:
        """Условие, проверяющее наличие ключа в словаре"""
        if "description" in transaction:
            """Если ключ найден, выводит назначение транзикции"""
            yield transaction["description"]
        else:
            yield ''

# if __name__ == '__main__':
#     for transaction in my_transactions:
#         transactions_date = transaction['date']
#         transaction_description = transaction['description']
#         print(process_bank_search(transactions_date), transaction_description)


