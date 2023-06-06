from utils.function import sort_list_json
from utils.function import value_correct
from utils.function import sort_date
from utils.function import hides_card_number
from utils.function import hide_account_number


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
