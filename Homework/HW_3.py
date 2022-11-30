# 1- Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих
# на нечётной позиции.
#
# Пример:
#
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint
from random import sample
from random import uniform
from random import shuffle
import re

def summ_odd_index (lenght: int)->int:
    """
       Находит сумму элементов списка, стоящих
    на нечётной позиции
       Args:
           lenght: int
       Returns:
           int - сумма элементов
    """
    summ=0
    lst = list(sample(range(-10, 10), lenght))
    for item in lst:
        if lst.index(item)%2 == 1:
            summ += item
    print(f'Сумма элементов с нечетным индексом в списке {lst} равна {summ}')

# summ_odd_index (5)

# 2-Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
#
# Пример:
#
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

def product_first_end_num_etc (lenght: int)->int:
    """
        Функция находит произведение пар чисел списка
    (первый и последний элемент,
    второй и предпоследний и т.д)
       Args:
           lenght: int (количество элементов в списке)
       Returns:
           int - сумма элементов
    """
    lst = list(sample(range(-10, 10), lenght))
    new_list = []
    for item in lst: #Как таки вот в этом месте сделать условие выхода
        product = item * lst[(len(lst)-1)-lst.index(item)]
        new_list.append(product)
        if len(new_list) >= len(lst)/2:
            break
    print(f'''
    Первоначальный список элементов: {lst}
    Список с произведениями элементов: {new_list}''')

# product_first_end_num_etc(5)

# 3-Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и
# минимальным значением дробной части элементов.
#
# Пример:
#
# [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
# [4.07, 5.1, 8.2444, 6.9814] - 0.9114 или 9114

def difference_max_min_el_after_point(lenght: int) -> int:
    """
            Функция находит разницу между максимальным и
        минимальным значением дробной части элементов
           Args:
               lenght: int (количество элементов в списке)
           Returns:
               int - разность элементов
        """
    # создали рандом для флоат
    list = []
    for i in range(lenght):
        x = round(uniform(0, 10), 5)
        list.append(x)
    new_list = []
    for i in range(0, len(list), 2):
        y = round(list[i], 1)
        new_list.append(y)
    for i in range(1, len(list), 4):
        y = round(list[i], 4)
        new_list.append(y)
    for i in range(2, len(list), 3):
        z = round(list[i], 3)
        new_list.append(z)
    res_list = sample(new_list, len(new_list))
    fraction_list = []
    for item in res_list:
        d = str(item).split('.')
        fraction = int(d[1])
        fraction_list.append(fraction)

    last_freaction = []
    for item in fraction_list:
        if item < 10:
            last_freaction.append(item * 1000)
        elif 10 <= item < 100:
            last_freaction.append(item * 100)
        elif 100 <= item < 1000:
            last_freaction.append(item * 10)
        else:
            last_freaction.append(item)

    res = max(last_freaction)
    res = str(res).strip('0')
    print(f'''Исходный список: {list},
Результирующий список: {fraction_list}, 
Результат: {res}
''')

# difference_max_min_el_after_point (10)


# 4- Напишите программу, которая будет преобразовывать десятичное число в двоичное. Подумайте, как это можно
# решить с помощью рекурсии.
# Не использовать функцию bin
#
# Пример:
#
# 45 -> 101101
# 3 -> 11
# 2 -> 10

def convert_int_to_bin(num: int, list = []) -> list:
    """
            Функция преобразовывает десятичное число в двоичное

        Args:
        num: int

        Returns:
        "list": бинарное выражение числа

    """
    if num <= 0:
        return list[::-1]
    else:
        x = num%2
        list.append(x)
        num = int(num/2)
        convert_int_to_bin(num)
        return list[::-1]


# print(f'Представление агрумента в бинарном виде: {convert_int_to_bin(10)}')
# print(bin(10))
# 5-Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#
# Пример:
#
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи
#
# Решение оформлять в виде функций
# По возможности добавляйте docstring

def show_fibonachi_minus_to_plus(num: int, list = []) -> list:
    """
            Функция отображает список чисел Фибоначчи (отрицательные и положительные значения)

        Args:
        num: int
        Returns:
        list: list

    """
    list_1 = []
    f1 = 0
    f2 = 1
    for _ in range(num):
        list_1.append(f1)
        f1,f2 = f2, f1 + f2
    list_1.pop(0)
    list_2 = []
    p1 = 0
    p2 = -1
    for _ in range(0,(-1*num),-1):
        list_2.append(abs(p1)*-1)
        p1, p2 = p2, p1 - p2

    list = list_2[::-1] + list_1
    return print(list)

show_fibonachi_minus_to_plus(15)
#(Дополнительно для навыков работы со словарями) *
# 6 - Бухгалтер Люба заполняет ведомость по зарплате. У Любы есть два файла - один с фио, другой - с зарплатой за декабрь.
#
# Ей нужно создать третий файл вида "фио, зарплата".
# Но Люба совершила ошибку. Она забыла, что в декабре все работники должны получить зарплату по повышенному коэффициенту: 1.5
# А еще у босса есть список любимчиков, которым повышенный коэффициэнт будет 2, их фио нужно выделить высоким регистром: они получат зарплату раньше.
# Создайте сначала словарь на основе первых двух файлов, а дальнейшие действия - с созданным словарем.
#
# Пример:
# Файл 1: (разумеется, у вас больше)
# Гарри Джеймс Поттер
# Дадли Вернон Дурсль
#
# Файл 2:
# 10000
# 12000
#
# Финальный файл:
# Гарри Джеймс Поттер, 15000
# ДАДЛИ ВЕРНОН ДУРСЛЬ 24000