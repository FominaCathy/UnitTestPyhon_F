"""тесты для класса MyList"""
import pytest
import yaml
from mylist import MyList

with open('database.yaml', encoding='utf-8') as fy:
    db_test = yaml.safe_load(fy)


@pytest.mark.parametrize("list_exe, exe", db_test['exec'])
def test_average_valid(list_exe, exe):
    """
    проврека расчета среднего для списков с валидными значениями
    :param list_exe: лист с данными
    :param exe: результат для сравнения
    :return:
    """
    assert MyList(list_exe).average == exe


def test_average_empty():
    """
    проверка возврата None для пустого списка
    :return:
    """
    assert MyList([]).average is None


def test_average_invalid():
    """
    проверка возврата None для листа с нечисловыми элементами
    :return:
    """
    assert MyList(db_test['list_bad']).average is None


def test_greater_mylist():
    """
    проверка переопределения сравнения "больше"
    :return:
    """
    assert MyList(db_test['list_big']) > MyList(db_test['list_smoll'])


def test_greater_or_equal_mylist():
    """
    проверка переопределения сравнения "больше либо  равно"
    :return:
    """
    assert MyList(db_test['list_smoll']) <= MyList(db_test['list_big']) \
           <= MyList(db_test['list_equal_big'])


def test_less_mylist():
    """
    проверка переопределения сравнения "меньше"
    :return:
    """
    assert MyList(db_test['list_smoll']) < MyList(db_test['list_big'])


def test_less_or_equal_mylist():
    """
    проверка переопределения сравнения "меньше либо равно"
    :return:
    """
    assert MyList(db_test['list_smoll']) <= MyList(db_test['list_big']) \
           and MyList(db_test['list_equal_big']) <= MyList(db_test['list_big'])


def test_equal_mylist():
    """
    проверка переопределения сравнения "равно"
    :return:
    """
    assert MyList(db_test['list_equal_big']) == MyList(db_test['list_big'])


def test_no_equal_mylist():
    """
    проверка переопределения сравнения "не равно"
    :return:
    """
    assert MyList(db_test['list_smoll']) != MyList(db_test['list_big'])
