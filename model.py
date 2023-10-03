"""основной модуль с функциями"""
from mylist import MyList


def compare_average(list_first: list, list_second: list):
    """
    Сравнивает средние значения списков:
    :param list_first: первый список для сравнения
    :param list_second: второй список для сравнения
    :return: строка:
    - ""Первый список имеет большее среднее значение"", если среднее значение первого списка больше.
    - ""Второй список имеет большее среднее значение"", если среднее значение второго списка больше.
    - ""Средние значения равны"", если средние значения списков равны.
    """

    try:
        first = MyList(list_first)
        second = MyList(list_second)
        result = ''
        if first > second:
            result = "Первый список имеет большее среднее значение"
        if first < second:
            result = "Второй список имеет большее среднее значение"
        if first == second:
            result = "Средние значения равны"
    except TypeError:
        return 'что-то пошло не так'
    return result
