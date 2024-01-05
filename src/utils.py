import json
import datetime


def load_operations(path):
    """Функция распаковывает json-файл"""
    with open(path, encoding="utf-8") as file:
        list_transfer = json.loads(file.read())
    return list_transfer

def get_date(transfers_list):
    ex_peration_list = [item for item in transfers_list if
                        item.get('state') == "EXECUTED"]
    ex_peration_list.sort(key=lambda x: x.get('date'),
                          reverse=True)
    return ex_peration_list[:5]

def get_formated_operation(operations):
    """Первая полоса вывода"""
    for operation in operations:
        formated_date = formate_date(operation['date'])
        type_operation = operation['description']
        line_one_output = f"{formated_date} {type_operation}"
        print(line_one_output)

        """Второя полоса вывода"""
        hided_from = hide_requisites(operation.get('from', ""))
        hided_to = hide_requisites(operation.get('to', ""))
        line_two_output = f"{hided_from} -> {hided_to}"
        print(line_two_output)

        """Третья полоса вывода"""
        amount = operation['operationAmount']['amount']
        currency = operation['operationAmount']['currency']['name']
        line_three_output = f"{amount} {currency}"
        print(line_three_output)
        print()

def hide_requisites(card_number: str):
    """Функция прячет номера карт и счетов"""
    list_card_info = card_number.split()
    new_list = []
    for info in list_card_info:
        if 'счет' in card_number.lower() and info.isdigit():
            new_list.append(f'**{info[-4:]}')
        elif 'счет' not in card_number.lower() and info.isdigit():
            new_list.append(
                f'{info[:4]} {info[4:6]}** **** {info[-4:]}')
        else:
            new_list.append(info)
    return ' '.join(new_list)


def formate_date(date):
    return datetime.datetime.fromisoformat(date).strftime('%d.%m.%Y')
