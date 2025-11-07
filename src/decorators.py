import time
from functools import wraps
from typing import Optional


def log(filename: Optional[str] = None):
    """Декоратор, который будет автоматически логировать начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки."""

    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            try:
                start_time = time.time()
                result = func(*args, **kwargs)
                end_time = time.time()
                log_message = (
                    f"Функция: {func.__name__}\nВремя начала выполнения функции: {start_time}\n"
                    f"Время окончания выполнения функции: {end_time}\nРезультат: {result}\n"
                )
                if filename:
                    with open(filename, "a", encoding="utf-8") as log_file:
                        log_file.write(log_message)
                else:
                    print(log_message)
                return result

            except Exception as e:
                error_message = (f"Функция: {func.__name__}\n Тип ошибки: {type(e).__name__}\n "
                                 f"Входные параметры: {args}, {kwargs}\n")
                if filename:
                    with open(filename, "a", encoding="utf-8") as log_file:
                        log_file.write(error_message)
                else:
                    print(error_message)
                raise

        return inner

    return wrapper


@log(filename="../mylog.txt")
def my_function(x, y):
    return x + y


print(my_function(2, 3))
