from src.utils import get_first_line, get_second_line , get_file , get_third_line , get_operation_list

coll = [
    {"date": "2019-08-26T10:50:58.294041", "state": "EXECUTED", },
    {"date": "2019-07-03T18:35:29.512364", "state": "CANCELED"},
    {}
]

col_date = {"date": "2019-08-26T10:50:58.294041",
            "description": "Перевод организации"}

col_second_line = {"from": "Maestro 1596837868705199",
                   "to": "Счет 64686473678894779589"}

col_second_line1 = {"from": "Счет 27248529432547658655",
                    "to": "Счет 97584898735659638967"}
col_second_line2 = {"from": "Visa Platinum 2256483756542539",
                    "to": "Счет 78808375133947439319"}
col_second_line3 = {"from": "Счет 17066032701791012883",
                    "to": "Visa Classic 4195191172583802"}
col_second_line4 = {"to": "Visa Classic 4195191172583802"}

amaunt_col = {"operationAmount": {"amount": "49192.52", "currency": {
    "name": "USD",
    "code": "USD"}}}

def test_get_operation_list():
    assert get_operation_list(coll) == [{"date": "2019-08-26T10:50:58.294041", "state": "EXECUTED", }]


def test_get_first_line():
    assert get_first_line(col_date) == '26.08.2019 Перевод организации'


def test_get_second_line():
    assert get_second_line(col_second_line) == 'Maestro 1596 83** **** 5199 -> Счет **9589'
    assert get_second_line(col_second_line1) == 'Счет **8655 -> Счет **8967'
    assert get_second_line(col_second_line2) == 'Visa Platinum 2256 48** **** 2539 -> Счет **9319'
    assert get_second_line(col_second_line3) == 'Счет **2883 -> Visa Classic 4195 19** **** 3802'
    assert get_second_line(col_second_line4) == '-> Visa Classic 4195 19** **** 3802'

def test_third_line():
    assert get_third_line(amaunt_col) == '49192.52 USD.'