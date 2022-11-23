# print("hello world")
# Переменные
# Используем динамическую типизацию
# int, float, boolean, str, list и др
# a = 123
# b = 1.23
# print(type(a))
# print(type(b))
# value = None
# s = 'hello "world"'
# print(s)
# print(a,'--', b, s)
# print('{1} - {2} - {0}'.format(a, b, s))
# print(f'{a} - {b} - {s}')

# f = False
# p = True
# print(p)

# # Списки в Питоне
# list = ["1","2",2, True] #Так можно но не нужно
# print(list)
# # Повнимательнее с пробелами в коде

# # Ввод и вывод данных
# print('Ввведите a')
# a = int(input())
# print('Ввведите b')
# b = int(input())
# print(a + b)

# # Арифметические операции

# a = + 123 #унарный плюс и минус.обычно плюс не пишут
# b = - 321
# c=a+b
# print(c)

# a = 2
# b = 8
# c=a/b
# print(c)
# # Выдает не целое число в отличие от шарпов
# # Для деления в целых числах используем
# a = 12
# b = 8
# c=a//b
# print(c)
# # Остаток от деления такой же как в шарпах
# a = 12
# b = 8
# c=a%b
# print(c)
# # Возведение в степень
# a = 2
# b = 4
# c=a**b
# print(c)
# # В питоне нет границы данных которые можно хрнить в числе
# a = 1.3
# b = 3
# c=round(a*b,1) #Вторым аргументов указываем колво знаков после запятой
# print(c)
# # Сложение и присваивание как в шарпах
# a = 3
# a += 5
# print(a)

# Логические операции

# a = 1<4 and 5>2 && конъюнкция
# a = 1==1 # Также можно сравнивать списки и строки
# a = 1<3<5<10<11<20<18 #Можно использовать тройные неравенства и больше
# f = 1>2 or 4<6 #|| дезъюнкция

# f =[1,2,3,4]
# print(f)
# print(not 2 in f) # смотрим есть ли элемент в списке или отрицание данного факта not

# is_odd = f[0] % 2 == 0 #обратились по индексу в списке к элементу
# print(is_odd) #проверили на четность и нечетность

# Управляющие конструкции if/else
# a = int(input('a = '))
# b = int(input('b = '))
# if a>b:
#     print(a) #отступ при ветвлении обязателен
# else:
#     print(b)
# при нескольких условиях
# if условие:
# elif условие:
# elif условие:

# Управляющая конструкции while

# while условие:
#     выполняем операции
# else:
#     выполняем операции после выхода из цикла

# Управляющая конструкции for

# for i in enumeration(итерируемый объект,например список):
#     выполняем операции
#     выполняем операции
# list = [1,2,3,4,5]
# for i in list:
#     print(i**2)

# list = range(10)
# for i in range(6,13, 2): #начало и конец интервала + приращение
#     print(i)

# for i in 'qwerty': #можно разбить по буквам
#     print(i)

# Работа со строками
# text = "КАК Я устал ОТ 44"
# print(len(text))
# print("от" in text)
# print(text.isdigit())
# print(text.islower())
# print(text.replace("устал", "УСТАЛ"))

# help(text.isdigit()) #узнать о методе

# Можно также обращаться к элементам строки по индексу
# print(text[0])
# print(text[-1]) #можно пойти с другой стороны
# print(text[:3]) #от нулевого до nго
# print(text[3:-2]) #берем интервал и т.д.

# Работа со списками list (есть езе range это разные типы данных)

# listok = [1,39,68,22]
# ran = (1,6,7,19)
# listok = list(ran) #приведение range к list/ можно сделать и обратное действие
# listok.append(654) #добавление элемента в конец списка
# listok.remove(654) #удаление по названию
# del listok[1] # по индексу
# print(listok)

# Функции


# def function_name(x):
#     if x == 1:
#         return "целое"
#     elif x == 2.3:
#         return 23
#     else:
#         return


# arg = 2
# print(function_name(arg))
# print(type(function_name(arg)))

# print('- Did Joffrey agree?\n- He did. He also said "I love using \\n\"')
# # - Did Joffrey agree?
# # - He did. He also said "I love using \n".

# stark = "Arya"

# print(f"Do you want to eat, {stark}?\nYes, I'm hungry, mom.")

# one_ = 'Naharis'
# two = 'Mormont'
# three = 'Sand'
# print(f'{one_[2]}{two[1]}{three[3]}{two[4]}{two[-5]}')

# value = 2
# value = 3
# string = "times"
# string_2 = str(value)
# print(string_2 + " " + string)

# number = -10.1234
# print(hex(round(number)))

# from random import randint
# print(randint(1,11))

# motto = 'Family, Duty, Honor'
# print(type(motto))

# print(number.__abs__())

# print(len.__doc__)

# text = "When \t\n you play a \t\n game of thrones you win or you die."
# print(text[6:17].strip().__len__())

# def say_hurray_three_times():

#     text = 'hurray!'
#     print(3*text)


# say_hurray_three_times()

# def truncate(text, cut_last_text):
#     return(text[:cut_last_text] + '...')

# def get_hidden_card(count_hide = 4, card = '2034399002121100') :
#     last_num = card[12:16]
#     return count_hide * "*" + last_num

# print(get_hidden_card())

# def trim_and_repeat(string, offset, repetitions):
#     return repetitions*(string[offset:])

# print (trim_and_repeat("булочка", 3, 3))

# def  get_age_difference(age1, age2):
#     return 'The age difference is ' + str(abs(age1 - age2))

# print (get_age_difference(1991, 1997))
# def has_upper_case(text):
#     if text == " " or text == "":
#         return False
#     elif text.islower() == True:
#         return False
#     else:
#         return True

# def has_upper_case(text):
#     return not text.strip().islower()

# print(has_upper_case(''))

# def is_leap_year(year):
#     return year % 400 == 0 or (year % 4 == 0 and not year % 100 == 0)

# print(is_leap_year(200))

# def string_or_not(info, str):
#    return type(info) == type(str) and 'yes' or 'no'

# print(string_or_not(4.5, 'блабла'))


# def normalize_url(str):
#     new_str = str [:8]
#     if 'http://' in new_str:
#         return 'https://' + str[7:]
#     elif 'https://' in new_str:
#         return 'https://' + str[8:]
#     else:
#         return 'https://' + str

# print(normalize_url('https://org/redirect-to?url=https://google.com'))

# a = 4
# a = a - 8 - a
# print(a)

# def print_numbers(num):
#     while(num>0):
#         print(num)
#         num -= 1
#     print('finished!')

# print_numbers(5)

# def join_numbers_from_range(start, finish):
#     initial_el = ""
#     i = start
#     while i <= finish:
#         new_str = str(i)
#         initial_el += new_str
#         i += 1
#     return initial_el
#
# print (join_numbers_from_range(5, 1000))

num = 10
print(type(num))
