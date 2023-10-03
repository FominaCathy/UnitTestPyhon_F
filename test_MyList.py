import pytest
from myList import MyList
import yaml

with open('database.yaml', encoding='utf-8') as fy:
    db_test = yaml.safe_load(fy)


@pytest.mark.parametrize("list_exe, exe", db_test['exec'])
def test_average_valid(list_exe, exe):
    assert MyList(list_exe).average == exe


def test_average_empty():
    assert MyList([]).average is None


def test_average_invalid():
    assert MyList(db_test['list_bad']).average is None


def test_greater_mylist():
    assert MyList(db_test['list_big']) > MyList(db_test['list_smoll'])


def test_greater_or_equal_mylist():
    assert MyList(db_test['list_smoll']) <= MyList(db_test['list_big']) <= MyList(db_test['list_equal_big'])


def test_less_mylist():
    assert MyList(db_test['list_smoll']) < MyList(db_test['list_big'])


def test_less_or_equal_mylist():
    assert MyList(db_test['list_smoll']) <= MyList(db_test['list_big']) \
           and MyList(db_test['list_equal_big']) <= MyList(db_test['list_big'])


def test_equal_mylist():
    assert MyList(db_test['list_equal_big']) == MyList(db_test['list_big'])


def test_no_equal_mylist():
    assert MyList(db_test['list_smoll']) != MyList(db_test['list_big'])


