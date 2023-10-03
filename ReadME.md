создан класс **MyList**
(расширение класса *list*)

для класса **MyList**

- определен метод расчета среднего (average):
  если в списке есть нечисловые элементы- average = None
- переопределены методы сравнения. списки сравниваются по среднему
  значению (сумма элементов)/(кол-во элементов)

Файл **model.py**

содержит метод **compare_average**

- принимает 2 списка, преобразует его в тип MyList
- возвращает:
    - *""Первый список имеет большее среднее значение""*, если среднее значение первого списка больше.
    - *""Второй список имеет большее среднее значение""*, если среднее значение второго списка больше.
    - *""Средние значения равны""*, если средние значения списков равны.

Тесты:

тестирование класса **MyList**

- расположены в файле **test_MyList.py**
- тестируется
    - метод расчета среднего для массива из нескольких элементов (когда результат целое число, вещественнное число,
      отрицательное число)
    - возвращение нуля при пустом массиве
    - возвращение None при невалидном массиве (если в массиве не числа)

тестирование метода **compare_average**

- расположен в файле **test_model.py**
- сценарии тестов:
    - возврщение текста "Первый список имеет большее среднее значение"
      если среднее значение первого списка больше
    - возвращение текста "Второй список имеет большее среднее значение",
      если среднее значение второго списка больше.
    - возвращение текста "Средние значения равны",
      если средние значения списков равны
    - проверка сравнения пустого и непустого валидного списка
    - проверка сравнения невалидного и валидного списков:
    - проверка сравнения пустого и списка со средним значением = 0
