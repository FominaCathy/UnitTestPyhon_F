import pytest
from model import compare_average
import yaml

with open('database.yaml', encoding='utf-8') as fy:
    db_test = yaml.safe_load(fy)


def test_compare_first_more_second(first_more_second):
    """
    проверка что если среднее значение первого списка больше - возвращается текст
    "Первый список имеет большее среднее значение"
    :param first_more_second: текст "Первый список имеет большее среднее значение"
    """
    assert compare_average(db_test['list_big'], db_test['list_smoll']) == first_more_second


def test_compare_second_more_first(second_more_first):
    """
    проверка что если среднее значение второго списка больше - возвращается текст
    "Второй список имеет большее среднее значение"
    :param first_more_second: текст "Второй список имеет большее среднее значение"
    """
    assert compare_average(db_test['list_smoll'], db_test['list_big']) == second_more_first


def test_compare_list_equals(first_equal_second):
    """
    проверка, что при сравнении списков с одинаковым средним возвращается текст "Средние значения равны"
    :param first_equal_second: "Средние значения равны"
    """
    assert compare_average(db_test['list_big'], db_test['list_equal_big']) == first_equal_second


def test_compare_list_invalid():
    """
    проверка, что при невалидном списке - программа не падает ошибка и возвращается сообщение 'что-то пошло не так'
    """
    assert compare_average(db_test['list_big'], db_test['list_bad']) == 'что-то пошло не так'


def test_compare_list_empty(second_more_first):
    """
    проверка сравнения пустого и непустого списка
    """
    assert compare_average([], db_test['list_big']) == 'что-то пошло не так'


def test_compare_zero_and_empty_list():
    """
    проверка сравнения нулевого и  пустого списков
    """
    assert compare_average([0], []) == 'что-то пошло не так'



