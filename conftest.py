import pytest

@pytest.fixture()
def first_more_second():
    return 'Первый список имеет большее среднее значение'


@pytest.fixture()
def second_more_first():
    return 'Второй список имеет большее среднее значение'


@pytest.fixture()
def first_equal_second():
    return 'Средние значения равны'