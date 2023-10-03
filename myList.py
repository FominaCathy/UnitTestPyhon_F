"""класс и его определение """
class MyList(list):
    """расширение класса list  с возможностью сравнивать по среднему значению """

    def __init__(self, mylist: list):
        super().__init__()
        self.my_list = mylist

    @property
    def average(self):
        """
        Рассчитывает среднее значение каждого списка.
        :param mylist: список для которого расчитыватся среднее значение
        :return: среднее значение, расчитанное по формуле: (сумма элементов)/(кол-во элементов).
                Если список пустой или расчитать среденее не удалось, то возвращается None
        """

        try:
            average = sum(self.my_list) / len(self.my_list)
        except ZeroDivisionError:
            return None
        except TypeError:
            return None
        return average

    def __eq__(self, other: list):
        return self.average == other.average

    def __lt__(self, other: list):  # меньше
        return self.average < other.average

    def __le__(self, other: list):  # меньше или =
        return self.average <= other.average

    def __gt__(self, other: list):
        return self.average > other.average

    def __ge__(self, other: list):
        return self.average >= other.average

    def __ne__(self, other: list):
        return self.average != other.average
