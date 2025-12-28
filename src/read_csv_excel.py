import json

import pandas as pd


def read_transactions_csv(csv_path: str) -> list:
    """Считывает финансовые операции из CSV-файла и возвращает список словарей с транзакциями"""
    try:
        df = pd.read_csv(csv_path)
        df_dict = df.to_dict("records")
        df_json = json.dumps(df_dict, ensure_ascii=False, indent=4)
        return df_json
    except FileNotFoundError:
        return []


# print(read_transactions_csv("../data/transactions.csv"))


def read_transactions_excel(excel_path: str) -> list[dict]:
    """Функция считывает финансовые операции из Excel - файла и выдает список
    словарей с транзакциями."""
    try:
        df_excel = pd.read_excel(excel_path)
        transactions = df_excel.to_dict(orient="records")
        return transactions
    except Exception:
        return []


# if __name__ == "__main__":
#     print(read_transactions_excel("../data/transactions_excel.xlsx"))
