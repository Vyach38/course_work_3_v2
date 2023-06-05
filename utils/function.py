import json
import os.path


def read_operations(file_path=os.path.join(os.path.dirname(__file__), 'operations.json')):
    with open(file_path, "r", encoding="utf-8") as file:
        result = json.load(file)
        return result


data = read_operations()


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


def sort_date(date):
    return sorted(date, key=lambda x: x['date'], reverse=True)
