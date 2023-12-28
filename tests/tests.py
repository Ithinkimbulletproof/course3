from os import path

from src.main import formate_date, get_date, load_operations


def test_get_transfers_list():
    assert load_operations(path) == [1, 2, 3]


def test_get_date():
    transfers = get_date
    transfers(path)
    assert get_date(
        [{'state': 'EXECUTED'}, {}, {'state': 'CANCELED'}]) == [
               {'state': 'EXECUTED'}]
    assert get_date(
        [{'state': 'EXECUTED'}, {}, {'state': 'CANCELED'}]) == [
               {'state': 'EXECUTED'}]


def test_formate_date():
    date = "2019-08-26T10:50:58.294041"
    assert formate_date(date) == (
        [{'date': '2018-01-21T01:10:28.317704'},
         {'date': '2018-12-18T17:07:09.800800'},
         {'date': '2019-12-08T22:46:21.935582'}]) == [
               {'date': '2019-12-08T22:46:21.935582'},
               {'date': '2018-12-18T17:07:09.800800'},
               {'date': '2018-01-21T01:10:28.317704'}]


def test_hide_requisites():
    assert hide_requisites(
        "Visa Gold 7305799447374042") == "Visa Gold 7305 79** **** 4042"
    assert hide_requisites(
        "Счет 96292138399386853355") == "Счет **3355"
