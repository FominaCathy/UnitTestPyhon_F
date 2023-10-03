from myList import MyList


def compare_average(list_first: list, list_second: list) -> str:
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
        if first > second:
            return f"Первый список имеет большее среднее значение"
        elif first < second:
            return "Второй список имеет большее среднее значение"
        elif first == second:
            return "Средние значения равны"
    except:
        return 'что-то пошло не так'
