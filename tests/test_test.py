from utils.function import sort_list_json
from utils.function import index_correct
from utils.function import sort_date


def test_sort_list_json(test_data_for_sort, expected_result_for_sort):
    assert sort_list_json(test_data_for_sort) == expected_result_for_sort


def test_list_correct():
    assert index_correct('2019-08-26T10:50:58.294041') == '2019.08.26'


def test_sort_date(test_date_correct, test_result_date_correct):
    assert sort_date(test_date_correct) == test_result_date_correct
