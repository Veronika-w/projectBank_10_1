from src.bank_operations import process_bank_search
from src.processing import sort_by_date
from src.read_csv_excel import read_transactions_csv, read_transactions_excel
from src.utils import read_json_operation


def main ():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n"
          "Выберите необходимый пункт меню:\n"
          "1. Получить информацию о транзакциях из JSON-файла\n"
          "2. Получить информацию о транзакциях из CSV-файла\n"
          "3. Получить информацию о транзакциях из XLSX-файла")