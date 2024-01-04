from src.utils import (load_operations, get_date,
                      get_formated_operation, hide_requisites)


def test_get_date():
    data = [{"date": "2019-04-04T23:20:05.206878",
             "state": "EXECUTED"},
            {"date": "2019-03-23T01:09:46.296404",
             "state": "EXECUTED"},
            {"date": "2018-12-20T16:43:26.929246",
             "state": "EXECUTED"}]
    expected = [{"date": "2019-04-04T23:20:05.206878",
                 "state": "EXECUTED"},
                {"date": "2019-03-23T01:09:46.296404",
                 "state": "EXECUTED"},
                {"date": "2018-12-20T16:43:26.929246",
                 "state": "EXECUTED"}]
    assert get_date(data) == expected

def test_load_operations():
    assert load_operations('tests/test_data.json') == [{}]

def test_get_formated_operation(capsys):
    test_operations = [{
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }]

    get_formated_operation(test_operations)
    captured = capsys.readouterr()
    assert captured.out == "26.08.2019 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет **9589\n31957.58 руб.\n\n"
    assert get_formated_operation(test_operations) is None

def test_hide_requisites():
    assert hide_requisites(
        "Счет 41421565395219882431") == "Счет **2431"
    assert hide_requisites(
        "Visa Platinum 8990922113665229") == "Visa Platinum 8990 92** **** 5229"
