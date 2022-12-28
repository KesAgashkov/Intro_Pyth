# def check_password(pas):
#     text = '!@#$%*'
#     count_sig = 0
#     count_num = 0
#     count_up = 0
#     if len(pas) < 10:
#         print('Easy peasy')
#     else:
#         for i in pas:
#             if i.isdigit():
#                 count_num +=1
#             if i.isupper():
#                 count_up += 1
#             for j in text:
#                 if i == j:
#                     count_sig += 1
#         if count_up > 0 and count_sig>0 and count_num>2:
#             print('Perfect password')
#         else:
#             print('Easy peasy')


# объявление функции
# def print_initials(name, surname, middlename):
#     surname = surname.capitalize()
#     name = name.capitalize()
#     middlename = middlename.capitalize()
#     return print(f'{surname} {name[0]}.{middlename[0]}.')
# # считываем данные
# name = input()
# surname = input()
# middlename = input()
#
# # вызываем функцию
# print_initials(name, surname, middlename)

# def factorial(x):
#     if x == 0 or x == 1:
#         return 1
#     else:
#         return factorial(x-1) * x

#
# def generate_fizz_buzz_list(n):
#     spis = []
#     for i in range(1,n+1):
#         if i%3 == 0  and i%5 == 0:
#             spis.append('FizzBuzz')
#         elif i%3 == 0:
#             spis.append('Fizz')
#         elif i%5 == 0:
#             spis.append('Buzz')
#         else:
#             spis.append(i)
#     return spis
#
#
# new = []
# def find_duplicate(lst):
#     for i in lst:
#         if lst.count(i)>1 and i not in new:
#             new.append(i)
#     return new
#
#
# def first_unique_char(s):
#     l1 = []
#     for i in s:
#         if s.count(i)==1:
#             return s.index(i)
#     else:
#         return(-1)
#

def format_name_list(names):
    new = ''
    if len(names) == 0:
        return new
    else:
        for i in range(len(names)):
            if len(names) == 1:
                return names[i]['name']
            elif len(names) == 2:
                new += str(names[i]['name']) + ' и '
            else:
                if i < len(names)-2:
                    new += str(names[i]['name'])+', '
                else:
                    new += str(names[i]['name']) + ' и '
        else:
            new = new.rstrip('и ')
    new = new.rstrip(', ')

    return new


format_name_list([{'name': 'Bart'}, {'name': 'Lisa'}])


def get_domain_name(url):
    if 'http://' in url or 'https://' in url:
        url = url.partition('//')[-1]
    else:
        pass
    if 'www' in url:
        url = url.partition('.')[-1]
    else:
        pass

    url = url.partition('.')[0]
    return url


import math
def factorial(n):
    res = math.factorial(n)
    return res
def trailing_zeros(n):
    res = math.factorial(n)
    count = 0
    res = str(res)
    for i in range(len(res)-1,-1,-1):
        if res[i] == '0':
            count+=1
        else:
            return count

from typing import Optional
def first_repeated_word(text: str)-> Optional[str]:
    '''Находит первый дубль в строке'''
    lst=[]
    for i in text.split():
        if i not in lst:
            lst.append(i)
        else:
            if i in lst:
                return i
            else:
                return None


import string


def shift_letter(letter: str, shift: int) -> str:
    '''Функция сдвигает символ letter на shift позиций'''
    spis = string.ascii_lowercase
    ind = spis.index(letter)
    if shift == 0 or shift == 26 or shift == -26:
        return letter
    elif shift < 0:
        if shift < -26:
            ind2 = shift % -26
            return spis[ind + ind2]
        else:
            return spis[ind - shift]
    else:
        if (shift + ind) > 26:
            return spis[(shift + ind) % 26]
        else:
            return spis[ind + shift]


shift_letter('z', 5)



shift_letter('z', 5)
def caesar_cipher(text: str, shift: int)->str:
    """Шифр цезаря"""
    alph = string.ascii_lowercase
    spis = ''
    if shift == 0 or abs(shift) == 26:
        return text
    elif shift > 0:
        for i in range(len(text)):
            if text[i].isalpha():
                ind = (alph.index(text[i]) + shift)%26
                spis+=alph[ind]
            else:
                spis+=text[i]
        return spis
    else:
        for i in range(len(text)):
            if text[i].isalpha():
                ind = (alph.index(text[i]) - abs(shift))%26
                spis+=alph[ind]
            else:
                spis+=text[i]
        return spis


MIN_DRIVING_AGE = 18
def allowed_driving(name: str, age: int) -> None:
    if age >= MIN_DRIVING_AGE:
        print(f'{name} может водить')
    else:
        print(f'{name} еще рано садиться за руль')


# объявление функции
def replace(text: str, old: str, new: str = ''):
    new_text = ''
    for item in text:
        if item == old:
            new_text+=new
        else:
            new_text+=item
    return new_text


# объявление функции
def make_header(text: str, head: str = '1'):
    return  f'<h{head}>{text}</h{head}>'



def create_matrix(size = 3, up_fill=0, down_fill=0):
    mat = [[0]*size for i in range (size)]
    for i in range(size):
        for j in range(size):
            if i == j:
                mat[i][j] = i+1
            elif i>j:
                mat[i][j] = down_fill
            else:
                mat[i][j] = up_fill
    return mat

