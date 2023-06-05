from pprint import pprint

from utils.function import read_operations
from utils.function import sort_list_json
from utils.function import value_correct
from utils.function import sort_date


date = read_operations()
date_b = sort_list_json(date)


for i in date_b:
    i['date'] = value_correct(i['date'])

