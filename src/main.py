import json
from datetime import datetime, date, time

class Operations:
    def __init__(self):
        self.list_transfer = []

    def __repr__(self):
        return (f"Last user's operations\n"
                f"{self.list_transfer}")

    def load_operations(self):
        """Функция распаковывает json-файл"""
        with open(r"C:\PycharmProjects\course3\operations.json", encoding="utf-8") as file:
            self.list_transfer = json.loads(file.read())
        return self.list_transfer

    def get_executed_operations(self, transfers_list):
        """Функция показывает операции,
        которые имеют статус EXECUTED"""
        ex_operation_list = []
        for state in transfers_list:
            if state.get("state") == "EXECUTED":
                ex_operation_list.append(state)
        self.list_transfer = ex_operation_list
        return ex_operation_list

def main():
    operation = Operations()
    print(operation.load_operations())
    print(operation.get_executed_operations(operation.list_transfer))

main()