import os.path

from utils.function import sort_list_json, summa, from_operation_number
from utils.function import value_correct
from utils.function import sort_date
from utils.function import hides_card_number
from utils.function import hide_account_number
from utils.function import from_operation_card
from utils.function import read_json

def test_read_json(test_read_json_operations):
    assert read_json(os.path.join(os.path.dirname(__file__), "test_function_read_json.json")) == test_read_json_operations


def test_sort_list_json(test_data_for_sort, expected_result_for_sort):
    assert sort_list_json(test_data_for_sort) == expected_result_for_sort


def test_value_correct():
    assert value_correct('2019-08-26T10:50:58.294041') == '2019.08.26'


def test_sort_date(test_date_correct, test_result_date_correct):
    assert sort_date(test_date_correct) == test_result_date_correct


def test_hides_card_number():
    assert hides_card_number("1596837868705199") == "1596 83** **** 5199"


def test_hide_account_number():
    assert hide_account_number("35383033474447895560") == "****************5560"
    assert hide_account_number("33474447895560") == "**********5560"


def test_from_operation_card():
    assert from_operation_card("Maestro 1596837868705199") == 'Maestro 1596 83** **** 5199'
    assert from_operation_card("MasterCard 7158300734726758") == 'MasterCard 7158 30** **** 6758'


def test_summa():
    assert summa({'amount': '55985.82', 'currency': {'code': 'USD', 'name': 'USD'}}) == "55985.82 USD"


def test_from_operation_number():
    assert from_operation_number("Счет 75106830613657916952") == "Счет ****************6952"
