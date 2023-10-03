"""отпределение фикстур  с текстами ответов"""
import pytest


@pytest.fixture()
def first_more_second():
    """ ответ, если первый список больше"""
    return 'Первый список имеет большее среднее значение'


@pytest.fixture()
def second_more_first():
    """ ответ, если второй список больше"""
    return 'Второй список имеет большее среднее значение'


@pytest.fixture()
def first_equal_second():
    """ ответ, если списки равны"""
    return 'Средние значения равны'
