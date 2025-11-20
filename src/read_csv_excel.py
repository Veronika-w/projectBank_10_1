import json
from typing import Any, Dict

import pandas as pd


def read_transactions_csv(file_path: str) -> list:
    """Считывает финансовые операции из CSV-файла и возвращает список словарей с транзакциями"""
    df = pd.read_csv(file_path)
    df_dict = df.to_dict('records')
    df_json = json.dumps(df_dict, ensure_ascii=False, indent=4)
    return df_json


print(read_transactions_csv('../data/transactions.csv'))


def read_transactions_excel(file_path: str) -> list[Dict[str, Any]]:
    """Функция считывает финансовые операции из Excel - файла и выдает список
    словарей с транзакциями."""
    try:
        df_excel = pd.read_excel(file_path)
        df_excel['id', 'amount'] = df_excel['id', 'amount'].astype(int)
        print(df_excel.to_dict(orient='records'))
    except FileNotFoundError:
        return []


if __name__ == "__main__":
    print(read_transactions_excel("C:/Users/PB/Desktop/Python/homework_10_1/data/transactions_excel.xlsx"))