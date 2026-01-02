import os
from src.bank_operations import process_bank_search
from src.processing import sort_by_date, filter_by_state
from src.read_csv_excel import read_transactions_csv, read_transactions_excel
from src.utils import read_json_operation


json_path = os.path.join(os.getcwd(), "data", "operations.json")
csv_path = os.path.join(os.getcwd(), "data", "transactions.csv")
excel_path = os.path.join(os.getcwd(), "data", "transactions_excel.xlsx")


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями. \n"
          "Выберите необходимый пункт меню:\n"
          "1. Получить информацию о транзакциях из JSON-файла\n"
          "2. Получить информацию о транзакциях из CSV-файла\n"
          "3. Получить информацию о транзакциях из XLSX-файла.")

    file_format = input()

    if file_format == '1':
        print("Для обработки выбран JSON-файл.")
        transactions = read_json_operation(json_path)
    elif file_format == '2':
        print("Для обработки выбран CSV-файл.")
        transactions = read_transactions_csv(csv_path)
    elif file_format == '3':
        print("Для обработки выбран XLSX-файл.")
        transactions = read_transactions_excel(excel_path)
    else:
        print("Неверный формат файла. Завершение работы.")
        return

    valid_states = ['EXECUTED', 'CANCELED', 'PENDING']
    state = ''
    while state not in valid_states:
        print("Введите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтрации статусы:", ', '.join(valid_states))
        state = input().strip().upper()

        if state not in valid_states:
            print(f"Статус операции '{state}' недоступен.")

    filtered_transactions = filter_by_state(transactions, state)
    print(filtered_transactions)
    print(f"Операции отфильтрованы по статусу '{state}'")


    sort_date = input("Отсортировать операции по дате? Да/Нет\n").strip().lower()
    if sort_date in ['да', 'yes']:
        sort_order = input("Отсортировать по возрастанию или по убыванию?\n").strip().lower()
        filtered_transactions = sort_by_date(filtered_transactions,
                                             reverse=(sort_order not in ['по возрастанию', 'ascending']))
    print(filtered_transactions)


    rub_filter = input("Выводить только рублевые транзакции? Да/Нет\n").strip().lower()
    if rub_filter in ['да', 'yes']:
        filtered_transactions = [tx for tx in transactions
    if tx.get('operationAmount', {}).get('currency', {}).get('code') == 'RUB']
        print(filtered_transactions)


    word_filter = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n").strip().lower()
    if word_filter in ['да', 'yes']:
        search_word = input("Введите слово для поиска:\n").strip().lower()
        filtered_transactions = process_bank_search(filtered_transactions, search_word)


    print("Распечатываю итоговый список транзакций...")
    print(filtered_transactions)
    if not filtered_transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")

main()
