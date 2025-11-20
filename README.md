
# Банковские операции клиента

## Описание

Этот проект предоставляет виджет для работы с банковскими операциями, позволяя фильтровать и сортировать транзакции.

## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/Veronika-w/projectBank_10_1.git
```
2. Установите зависимости:
```
pip install -r requirements.txt
```

## Использование
 
Пример использования функций:


from src.processing import filter_by_state, sort_by_date

list_dict = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

## Фильтрация по статусу
filter_status = filter_by_state(list_dict)

## Сортировка по дате
sorted_date = sort_by_date(list_dict)

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

## Фильтрация по транзакциям
filter_transact = filter_by_currency(list_transactions)

## Фильтрация по операциям
descrip_operation = transaction_descriptions(list_transactions)

## Вывод номера карты в формате XXXX XXXX XXXX XXXX
number_card = card_number_generator (0, 9999999999999999)

## Добавлен декоратор log 
который будет автоматически логировать начало и конец выполнения функции, а также ее результаты или возникшие ошибки.

## Тестирование
Для тестирование используется библиотека pytest.

Тестовое покрытие составляет более 80%. Для запуска тестов используется команда pytest 

## Обработка CSV и XLSX - файлов
Проект поддерживает обработку CSV и XLSX - файлов

## Авторы

Мазуренко Вероника Владиславовна


