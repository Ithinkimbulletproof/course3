import json
from datetime import datetime, date, time

def __init__(self):
    self.list_transfer = []

def __repr__(self):
    return(f"Last user's operations\n"
               f"{self.list_transfer}")

def load_operations(self):
    """Функция распаковывает json-файл"""
    with open("operations.json", encoding="utf-8") as file:
        self.list_transfer = json.loads(file.read())
    return self.list_transfer

def get_last_five_operations(self):
    """Функция показывает последние 5 операций"""
    five_list = []
    for state in self.list_transfer:
        ex_state = state.get('state')
        if ex_state == "EXECUTED":
            five_list.append(state)
        else:
            continue

    return five_list

print(get_last_five_operations())
#    def


