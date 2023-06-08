from utils.function import read_json, file_path
from utils.function import sort_list_json
from utils.function import value_correct
from utils.function import sort_date
from utils.function import from_operation_card
from utils.function import from_operation_number
from utils.function import summa

date = read_json(file_path)
date_b = sort_list_json(date)


for i in date_b:
    i['date'] = value_correct(i['date'])

list_sort_date = sort_date(date_b)

for date_list in list_sort_date[:5]:
    print()
    print(f"{date_list['date'][8:]}.{date_list['date'][5:7]}.{date_list['date'][:4]} {date_list['description']}")
    if date_list.get('from'):
        if 'Счет' not in date_list['from'] and 'Счет' not in date_list['to']:
                print(from_operation_card(date_list['from']) + ' ' + '->' + ' ' + from_operation_card(date_list['to']))
        if 'Счет' in date_list['from'] and 'Счет' in date_list['to']:
                print(from_operation_number(date_list['from']) + ' ' + '->' + ' ' + from_operation_number(date_list['to']))
        if 'Счет' not in date_list['from'] and 'Счет' in date_list['to']:
                print(from_operation_card(date_list['from']) + ' ' + '->' + ' ' + from_operation_number(date_list['to']))
        if 'Счет' in date_list['from'] and 'Счет' not in date_list['to']:
                print(from_operation_card(date_list['from']) + ' ' + '->' + ' ' + from_operation_number(date_list['to']))
    else:
        if 'Счет' not in date_list['to']:
            print(from_operation_card(date_list['to']))
        else:
            print(from_operation_number(date_list['to']))
    print(summa(date_list['operationAmount']))
