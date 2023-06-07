import json
import os.path


file_path = os.path.join(os.path.dirname(__file__), 'operations.json')

def read_json(file_path):
    """Получаем обЪект python из обЪекта json"""
    with open(file_path, "r", encoding="utf-8") as file:
        result = json.load(file)
        return result



def sort_list_json(date: list) -> list:
    """Создаём список с выполненными операциями"""
    sorted_data = []
    for position in date:
        for value in position.values():
            if value == 'EXECUTED':
                sorted_data.append(position)
    return sorted_data


def value_correct(value: str) -> str:
    """Изменяем значения ключа 'date'"""

    sep = '.'
    date = value[0:10]
    list_date = date.split("-")
    return list_date[0] + sep + list_date[1] + sep + list_date[2]


def sort_date(date: list) -> list:
    """Сортируем список словарей по дате операции"""

    return sorted(date, key=lambda x: x['date'], reverse=True)


def hides_card_number(number: str) -> str:
    """Скрываем номер карты"""

    hidden_number = number[0:6] + "*" * (len(number) - 10) + number[-4:]
    card_number = hidden_number[0:4] + ' ' + hidden_number[4:8] + ' ' + hidden_number[8:12] + ' ' + hidden_number[12:]
    return card_number


def hide_account_number(number: str) -> str:
    """Скрываем номер счёта"""

    account_number = "*" * (len(number) - 4) + number[-4:]
    return account_number


def from_operation_card(str_key: str) -> str:
    """выводим название карты и скрываем её номер"""
    key_from_list = str_key.split(" ")
    for element in key_from_list:
        if element.isdigit():
            hides_number = hides_card_number(element)
            return " ".join(key_from_list[:-1]) + " " + hides_number


def from_operation_number(dict_key: str) -> str:
    """Возвращаем 'Счет' и скрытый номер карты"""
    key_list = dict_key.split(" ")
    for element_1 in key_list:
        if element_1.isdigit():
            result_1 = hide_account_number(element_1)
            return " ".join(key_list[:-1]) + " " + result_1


def summa(dict_sum: dict) -> str:
    """Возвращает сумму перевода или вклада и в какой валюте"""
    return dict_sum['amount'] + " " + dict_sum['currency']['name']
