# Функция isinstance является встроенной функцией python
#
# И для того что-бы показать что она может делать давайте создадим список а:
#
# a = [1, 2, '3', '4', [5, '6'], (7,'8'), 9.0] – в этом списке есть типы данных: int, str, list, tuple, float.
#
# Чтобы убедиться в этом можно сделать такое выражение:
#
# for  i in a:
#
#          print(i, type(i))
#
# Вывод:
#
# 1 <class 'int'> - число
#
# 2 <class 'int'> - число
#
# 3 <class 'str'> - строка
#
# 4 <class 'str'> - строка
#
# [5, '6'] <class 'list'> - список
#
# (7, '8') <class 'tuple'> - кортеж
#
# 9.0 <class 'float'> - вещественное число
#
# Теперь давайте заведем перебенную b в которой будем считать сумму всех чисел:
#
# b = 0
#
# for i in a:
#
#          b += i
#
# print(b)
#
# Вывод: TypeError: unsupported operand type(s) for +=: 'int' and 'str' – эта ошибка гласит что нельзя к числу прибавлять строку, этой строкой был элемент ‘3’
#
# И чтобы решить данную проблему, на помощь приходит функцию isinstance()
#
# Функция isinstance принимает на вход два аргумента, первый аргумент это какой либо обьект, второй аргумент это тип обекта.
#
# Тоесть эта функция проверяет является ли первый аргуемент инстанцией второго аргумента:
#
# Isinstance возвращает bool:
#
# print(isinstance(1, int)) – здесь мы первым аргументом передали цифру 1, а вторым аргументом тип обьекта int, и так как цифра 1 является типом обьекта Int, функция isinstance Вернут True
#
# И это очень полезно, например будем использовать эту функцию для проверки обьекта i в цикле for
#
# a = [1, 2, '3', '4', [5, '6'], (7,'8'), 9.0]
#
# b = 0 – сюда будем складывать все цифры обьекта Int
#
# for i in a:
#          if isinstance(i, int) – тоесть проверяется является ли элемент i Обьектом типа int, и если функция isinstance вернет True То выполнится код в блоке условия.
#
#          b += i прибавляем к b проверенный элемент i
#
# Вывод: 3, первые два элемента это 1, 2 их сумма равняется 3, дальше 3 и 4 это строки (str) – они проверку не проходят, дальше список с элементами 5(int), 6(str) они не будут складываться так как они внутри вложенного списка и в функцию isinstance попадают не они а сам список и так как список не Int а лист, проверку не проходит, с tuple тоже самое а 9.0 это float (вещественное число)
#
# В функцию isinstance() вторым аргументом можно передавать все существующие типы обьектов в python:
#
# Int, str, list, tuple, dict, file, float, set, bool.

# пример
# def count_strings(*args):
#     s = 0
#     for i in args:
#         if isinstance(i, str):
#             s += 1
#     return s


def find_keys(**kwargs):
    dic = dict(kwargs)
    spis = []
    for k,v in dic.items():
        if isinstance(v, (tuple,list)):
            spis.append(k)
    spis = sorted(spis, key=str.lower)
    return spis


find_keys(t=[4, 5], W=[5, 3], A=(3, 2), a={2, 3}, b=[4])