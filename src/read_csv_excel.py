import pandas as pd


def read_transactions_csv(csv_path: str) -> list[dict]:
    """Считывает финансовые операции из CSV-файла и возвращает список словарей с транзакциями"""
    try:
        df_csv = pd.read_csv(csv_path)
        # print(df.head())
        df_dict_csv = df_csv.to_dict("records")
        # print(df_dict)
        return df_dict_csv
    except FileExistsError:
        return []

# if __name__ == "__main__":
#     print(read_transactions_csv("../data/transactions.csv"))


def read_transactions_excel(excel_path: str) -> list[dict]:
    """Функция считывает финансовые операции из Excel - файла и выдает список
    словарей с транзакциями."""
    try:
        df_excel = pd.read_excel(excel_path)
        df_dict_excel = df_excel.to_dict(orient="records")
        return df_dict_excel
    except Exception:
        return []


# if __name__ == "__main__":
#     print(read_transactions_excel("../data/transactions_excel.xlsx"))
