import pathlib
from src.utils import load_operations, get_formated_operation, get_date

def main():
    path = pathlib.Path(__file__).parent.parent.joinpath('operations.json')
    load_operations(path)
    list_transfer = load_operations(path)
    get_date(list_transfer)
    sorted_operations = get_date(list_transfer)
    get_formated_operation(sorted_operations)

main()
