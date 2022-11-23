# def is_square_number(first_num, sec_num):
#     summ = 0
#     while summ <= sec_num:
#         summ *= first_num
#     if summ == sec_num:
#         return True
#     else:
#         return False

# print(is_square_number(5, 25))

# 3- Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

# *Примеры:*

# - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5
# 4-Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.

# *Примеры:*

# - 6,78 -> 7
# - 5 -> нет
# - 0,34 -> 3

# num_n = abs(int(input("Введите число ")))
# start = num_n * -1
# new_range = range(start,num_n+1)
# for i in new_range:
#     print(i,end = "  ")

import math
num_n = float(input("Введите дробное число "))
num = round(num_n * 10, 1)
print(num)
result = num % 10
print(math.floor(result))

