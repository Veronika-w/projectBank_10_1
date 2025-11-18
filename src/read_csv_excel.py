import csv
import pandas as pd
from typing import Any, Dict


def read_transactions_csv(file_path: str) -> list:
    """Считывает финансовые операции из CSV-файла и возвращает список словарей с транзакциями"""
    try:
        transactions_csv = []
        with open(file_path, 'r', newline='', encoding='utf-8') as csv_file:
            rd_transactions_csv = csv.DictReader(csv_file)
            next(rd_transactions_csv)
            for row in rd_transactions_csv:
                transactions_csv.append(row)
        return transactions_csv
    except FileNotFoundError:
        return []


if __name__ == "__main__":
    print(read_transactions_csv("C:/Users/i3/my_pj/pythonBank/data/transactions.csv"))


def read_transactions_excel(file_path: str) -> list[Dict[str, Any]]:
    """Функция считывает финансовые операции из Excel - файла и выдает список
    словарей с транзакциями."""
    try:
        df = pd.read_excel(file_path)
        df['id', 'amount'] = df['id', 'amount'].astype(int)
        print(df.to_dict(orient='records'))

    except FileNotFoundError:
        return []


if __name__ == "__main__":
    print(read_transactions_excel("C:/Users/i3/my_pj/pythonBank/data/transactions_excel.xlsx"))
