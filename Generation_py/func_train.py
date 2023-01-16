# объявление функции
# def is_valid_triangle(side1, side2, side3):
#     return (side1+side2)>side3 and (side1+side3)>side2 and (side2+side3)>side1
#
# # считываем данные
# a, b, c = int(input()), int(input()), int(input())
#
# # вызываем функцию
# print(is_valid_triangle(a, b, c))
#
#
# # объявление функции
# def is_prime(num):
#     if num == 1:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     else:
#         return True
#
#
# def get_next_prime(num):
#     for i in range(num+1,num+1000):
#         for j in range(2,i):
#             if i % j == 0:
#                 break
#         else:
#             return i
#             break

# def is_password_good(password):
#     if len(password)> 8 and password.isalpha() and not password.islower() and not password.isupper():
#         return True
#     else:
#         return False
#
#
# def is_one_away(word1, word2):
#     cou = 0
#     if len(word1) == len(word2):
#         for i in range(len(word1)):
#             if word1[i] != word2[i]:
#                 cou+=1
#         else:
#             if cou == 1:
#                 return True
#             else:
#                 return False
#     else:
#         return False
#
# def is_palindrome(text):
#     text =text.replace(" ", "").replace(".", "").replace("!", ""). replace("?", "").replace("-", ""). replace(",", "").lower()
#     if text == text[::-1]:
#         return True
#     else:
#         return False
#
#
# def is_valid_password(password):
#     password = password.split(':')
#     if password[0] == password[0][::-1] and int(password[2])%2==0 and len(password)==3:
#         for i in range(2,int(password[1])):
#              if int(password[1])%i == 0:
#                     return False
#         else:
#             return True
#     else:
#         return False
#
#
# def is_correct_bracket(text):
#     check = 0
#     if text[0] == ')' or text[-1] == '(' or text.count('(')!= text.count(')'):
#         return False
#     for i in text:
#         if i==')' and check == 0:
#             return False
#         if i == '(':
#             check -=1
#         else:
#             check +=1
#     if check == 0:
#         return True
#     else:
#         return False
#
#
# def convert_to_python_case(text):
#     res = ''
#     for i in text:
#         if i.isupper():
#             res+='_'+i.lower()
#         else:
#             res+=i
#     return res.strip('_')
#
#
# import math
#
#
# def solve(a, b, c):
#     r = []
#     res = b ** 2 - 4 * a * c
#     if res < 0:
#         return
#     elif res == 0:
#         return -b / (2 * a), -b / (2 * a)
#     else:
#         r.append((-b + math.sqrt(res)) / (2 * a))
#         r.append((-b - math.sqrt(res)) / (2 * a))
#         x1 = min(r)
#         x2 = max(r)
#         return x1, x2
#
#
# # считываем данные
# a, b, c = int(input()), int(input()), int(input())
#
# # вызываем функцию
# x1, x2 = solve(a, b, c)
# print(x1, x2)
#
#
# def draw_triangle():
#     for i in range(1,9*2-1,2):
#         print((i*'*').center(15).rstrip())
#
#
# from math import factorial
# def compute_binom(n, k):
#     return int((factorial(n))/(factorial(k)*factorial(n - k)))
#
# # считываем данные
# n = int(input())
# k = int(input())
#
# # вызываем функцию
# print(compute_binom(n, k))
#
#
# # объявление функции
# def number_to_words(num):
#     se = ['', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять', 'одиннадцать',
#           'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать',
#           'девятнадцать']
#     sd = ['', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
#     if n < 20:
#         return se[n]
#     elif n % 10 == 0 and n > 19:
#         return sd[n // 10 - 1]
#     else:
#         return str(sd[n // 10 - 1]) + ' ' + str(se[n % 10])
#
#
# # считываем данные
# n = int(input())
#
# # вызываем функцию
# print(number_to_words(n))# объявление функции



# def number_to_words(num):
#     se = ['','один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
#     sd = ['', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
#     if n < 20:
#         return se[n]
#     elif n%10 == 0 and n>19:
#         return sd[n//10-1]
#     else:
#         return str(sd[n//10-1]) + ' ' + str(se[n%10])
#
#
# # считываем данные
# n = int(input())
#
# # вызываем функцию
# print(number_to_words(n))
#
#
# # объявление функции
# def is_magic(date):
#     a,b,c = date.split('.')
#     if int(a)*int(b) == int(c[2:]):
#         return True
#     else:
#         return False
# # считываем данные
# date = input()
#
# # вызываем функцию
# print(is_magic(date))
#
#
# # объявление функции
# def is_pangram(text):
#     text = text.lower()
#     text = set(text)
#     if len(text)-1 == 26:
#         return True
#     else:
#         return False
#
# # считываем данные
# text = input()
#
# # вызываем функцию
# print(is_pangram(text))
#
#
#
# from math import log2,ceil
# n = int(input())
# print(ceil(log2(n)))
#

from random import randrange, choice, shuffle
#
# def veri():
#     try:
#         num = int(input('Введите целое число\n>'))
#         while 0 > num or num > 100:
#             print('Ошибка. введите число еще раз')
#             num = int(input('Введите целое число\n>'))
#     except:
#         print('Ошибка. введите число еще раз')
#         num = int(input('Введите целое число\n>'))
#     return num
#
# def inter():
#     try:
#         num = int(input('Введите целое число\n>'))
#     except:
#         print('Ошибка, попробуйте еще раз')
#         inter()
#     return num
#
# def game():
#     print('Укажите интервалы для выбора случайного числа')
#     print('начало')
#     start = inter()
#     print('конец')
#     finish = inter()
#     secret = randrange(start,finish)
#     count = 0
#     print("Добро пожаловать в угадайку")
#     num = veri()
#     while True:
#         if secret == num:
#             print(f'Поздравляю, вы победили\nКоличество ваших попыток {count}')
#             break
#         elif num<secret:
#             print('Возьмите больше')
#             num = veri()
#             count+=1
#         else:
#             print('Возьмите меньше')
#             num = veri()
#             count+=1
#     resp = input('Хотите сыграть еще раз?\n да или нет')
#     if resp =='да':
#         game()
#     else:
#         pass
#
#
# def magic_bowl ():
#     resp = input('Напиши вопрос, на который хочешь получить ответ\n>')
#     resp1 = input('Ты уверен, что хочешь использовать черную магию???')
#     answers = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай",
#                "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
#                "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет",
#                "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"]
#     print(f'{resp}\n{answers[randrange(0,len(answers)-1)]}')
#     resp = input('Хочешь задать еще вопрос?\nда или нет\n>')
#     if resp == 'да':
#         magic_bowl ()
#     else:
#         pass
#
# def gener_pass():
#     print("Добро пожаловать в генератор пороля")
#     digits = '123456789'
#     lowercase_letters =  'abcdefghijklmnopqrstuvwxyz'
#     uppercase_letters =  'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     punctuation = '!# $%&*+-=?@^_.'
#     password = ''
#     res = []
#     flag =  True
#     print('Укажите количество паролей для генерации:')
#     cntPw = inter()
#     print('Укажите длину одного пароля:')
#     lenPw = inter()
#     digOn = input('Включать ли цифры 0123456789? (y/n)')
#     ABCon = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n)')
#     abcOn = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (y/n)')
#     chOn = input('Включать ли символы !#$%&*+-=?@^_? (y/n)')
#     for i in range(cntPw+1):
#         password = list(password)
#         shuffle(password)
#         res.append(''.join(password))
#         password = ''
#         while True:
#             if digOn == 'y':
#                 password+= choice(digits)
#                 if len(password) == lenPw:
#                     break
#             if ABCon == 'y':
#                 password += choice(uppercase_letters)
#                 if len(password) == lenPw:
#                     break
#             if abcOn == 'y':
#                 password += choice(lowercase_letters)
#                 if len(password) == lenPw:
#                     break
#             if chOn == 'y':
#                 password += choice(punctuation)
#                 if len(password) == lenPw:
#                     break
#
#     return print(*res[1:])
#
# gener_pass()
#
#
def caesar_code(n, text):
    const_lower_ru = 'абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя'
    new = ''
    for i in text:
        if i in text:
            shift = (const_lower_ru.find(i, i)+n)%len(const_lower_ru)
            new += const_lower_ru[shift]
    return print(new)


def caesar_code(n, text):
    const_lower_ru = 'абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя'
    new = ''
    for i in text:
        if i.lower() in const_lower_ru:
            sig = const_lower_ru.find(i.lower())
            shift = (sig + n) % len(const_lower_ru)
            if i.islower():
                new += const_lower_ru[shift]
            else:
                new += const_lower_ru[shift].upper()
        else:
            new += i
    return print(new)


caesar_code(17, "Шсъцхр щмчжмщ йшм, нмтзж йшм лхшщзщг.")


def caesar_code(n, text):
    const_lower_ru = 'abcdefghijklmnopqrstuvwxyz'
    new = ''
    res = []
    for sh in range(1, 26):
        res.append(new)
        new = ''
        for i in text:
            if i.lower() in const_lower_ru:
                sig = const_lower_ru.find(i.lower())
                shift = (sig + n) % len(const_lower_ru)
                if i.islower():
                    new += const_lower_ru[shift]
                else:
                    new += const_lower_ru[shift].upper()
            else:
                new += i
    return print(new)


caesar_code(25, "Sgd fqzrr hr zkvzxr fqddmdq nm sgd nsgdq rhcd ne sgd edmbd.")


# Вариант с изменяемым сдвигом в зависимости от длины слова


def caesar_code(text):
    sp = text.split()
    const_lower_ru = 'abcdefghijklmnopqrstuvwxyz'
    new = ''
    res = []
    for i in sp:
        n = len(i.replace('!', '').replace(',', '').replace('"', '').replace('.', ''))
        res += new
        new = ''
        for j in i:
            if j.lower() in const_lower_ru:
                sig = const_lower_ru.find(j.lower())
                shift = (sig + n) % len(const_lower_ru)
                if j.islower():
                    new += const_lower_ru[shift]
                else:
                    new += const_lower_ru[shift].upper()
            else:
                new += j
        else:
            res += [new]
            new = ''

    return print(*res)


caesar_code(input())



n = int(input())
print(bin(n)[2:])
print(oct(n)[2:])
print(hex(n)[2:].upper())

