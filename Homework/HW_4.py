# Урок 4. Данные, функции и модули в Python. Продолжение
# 1 - Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]
import math

def search_simple_multipliers(n: int) -> print:
    """
            Функция составляет список простых множителей числа N

        Args:
        num: int

        Returns:
        print
    """
    for i in range(2, int(math.sqrt(n)) + 1):
        while (n % i == 0):
            print(f"{i}", end=' ')
            n //= i

    if (n != 1):
        print(f'N = {n} --> {n}')


# search_simple_multipliers(8)
# 2 - Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной
# последовательности. Не использовать множества.
# Постарайтесь решить за одно условие
# [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]

def search_uniq_elts(elements: list) -> list:
    """
            Функция выведет список неповторяющихся элементов исходной
последовательности

        Args:
        list: int

        Returns:
        list: int
    """
    new_list = []
    index = 1
    new_list.append(elements[0])
    while index<len(elements)-1:
        if elements[index] != elements[index+1]:
            new_list.append(elements[index+1])
            index+=1
        else:
            index+=1
    return new_list,elements
#
# print(f'Красивый лист на выходе:{search_uniq_elts([1,1,1,1,2,2,2,3,3,3,4])}')
#
# 3 - В файле, содержащем фамилии студентов и их оценки, изменить на буквы в верхнем регистре тех студентов, которые
# имеют средний балл более «4».
# Нужно перезаписать файл.
# Пример:
# Ангела Меркель 5
# Энакин Скайуокер 5
# Фредди Меркури 3
# Александр Пушкин 4
#
# Программа выдаст:
# АНГЕЛА МЕРКЕЛЬ 5
# ЭНАКИН СКАЙУОКЕР 5
# Фредди Меркури 3
# Александр Пушкин 4


def write_to_file(str = '''Ангела Меркель 5
Энакин Скайуокер 5
Фредди Меркури 3
Александр Пушкин 4
Гоголь Моголь 5'''):
    with open ('file1.txt','w') as file:
        file.write(str)


def rewrite_data():
    # with open('file1.txt', 'r') as file:
    #         for line in file:
    #             if '5' in line:
    #                 new = line.upper()
    #                 file.write(new + '\n')

    with open('file1.txt', 'r') as file1, open('file2.txt', 'w') as text2:
        lines = file1.readlines()
        char = '5'
        for line in lines:
            if char in line:
                new_data = line.replace(line, line.upper())
                text2.write(new_data)
            else:
                text2.write(line)
write_to_file()
rewrite_data()

# 4- Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное количество символов влево
# или вправо. При расшифровке происходит обратная операция.
# К примеру, слово "абба" можно зашифровать "бввб" - сдвиг на 1 вправо. "вггв" - сдвиг на 2 вправо, "юяяю" -
# сдвиг на 2 влево.
# Сдвиг часто называют ключом шифрования.
# Ваша задача - написать функцию, которая записывает в файл шифрованный текст, а также функцию, которая спрашивает
# ключ, считывает текст и дешифровывает его.

# def cipher_cesarius_input(n_shift = int(input("Введите ключ шифрования от 1 до 35: "))
#                           ,str1 = (input("Введите текст для шифрования на русском языке: "))) -> str:
#         """
#                 Функция зашифровывает текст с выбранным сдвигом
#
#             Args:
#             n_shift: int - количество элементов для сдвига
#
#             Returns:
#             cifr_text: str - зашифрованный текст
#         """
#         alphabet = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя,.: абвгдеёжзийклмнопрстуфхцчшщъыьэюя,.: ')
#         str1 = str1.lower()
#         cifr_text = ''
#         for i in str1:
#             mesto = alphabet.index(i)
#             new_mesto = mesto + n_shift
#             if i in alphabet:
#                 cifr_text += alphabet[new_mesto]
#             else:
#                 print("Вы ввели недопустимое значение, попробуйте еще раз")
#                 break
#
#         with open ('file_code.txt', 'w') as file:
#             file.write(cifr_text)
#         return cifr_text


# print(f'Ваш зашифрованный текст: {cipher_cesarius_input()}')
# tex = cipher_cesarius_input()

# def transcrypt_cipher_cesarius(key = int(input("Введите ключ для дешифровки: "))) ->str:
#     """
#                    Расшифровывает текст
#
#                Args:
#                 key: int - ключ для разгадки шифра
#
#                Returns:
#                dechif_text: str - расшифрованный текст
#     """
#     with open('file_code.txt', 'r') as file:
#         chif_text = file.read()
#
#     alphabet = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя,. : абвгдеёжзийклмнопрстуфхцчшщъыьэюя,.: ')[::-1]
#     dechif_text = ''
#     for i in chif_text:
#         mesto = alphabet.index(i)
#         new_mesto = mesto + key
#         if i in alphabet:
#             dechif_text += alphabet[new_mesto]
#     with open('file_encode.txt', 'a') as file:
#         file.write(f'{dechif_text} \n')
#     return dechif_text


# print(f'ваш зашифрованный текст: {transcrypt_cipher_cesarius()}')

# 5 - Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся
# в отдельных текстовых файлах.
# файл первый:
# AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool
# файл второй:
# 12A11B10C6D5E4FG python is s7o c7ol
# Первая функция - текст зашифровывает
# Вторая - расшифровывает
# Две промежуточные - считывают с файла и записывают в файл
#
# Решения оформляйте в виде функций
# Используйте type hints и doctring

def write_to_file_task_5(str = 'AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool'):
    with open ('file_task_5.txt','w') as file:
        file.write(str)
write_to_file_task_5()

def convert_to_RLE_alg()->str:

    """
        Функция осуществляет кодирование длин серий (RLE)

        Returns:
                compr_text : str - сжатый текст
    """

    with open('file_task_5.txt', 'r') as file:
        text_for_compress = file.read()
    index = 0
    count = 1
    compr_text = ''
    text_for_compress += ' '
    while index < len(text_for_compress)-1:
        if text_for_compress[index].isdigit():
            compr_text += text_for_compress[index]
            index+=1
        elif text_for_compress[index] == text_for_compress[index + 1]:
            count += 1
            index += 1
        elif text_for_compress[index] != text_for_compress[index + 1]:
            if count ==1:
                compr_text += text_for_compress[index]
            else:
                compr_text += str(count) + text_for_compress[index]
            count = 1
            index += 1
        elif index.text_for_compress[index] == -1:
            compr_text+=text_for_compress[index]
    with open('file_task_5_compr', 'w') as file:
        file.write(compr_text)
    return compr_text, len(text_for_compress)


    return compr_text

# print(f'Выходной текст и длина первоначального текста:{convert_to_RLE_alg()}')
compr_text, prime_lenght = convert_to_RLE_alg()


def recompression_RLE_to_text()->str:

    """
        Функция осуществляет распаковку сжатого текста

        Returns:
                long_text : str - распакованный текст
    """
    with open('file_task_5_compr', 'r') as file:
        text_from_file = file.read()
    index = 0
    count = ''
    compr_text = ''
    while index < len(text_from_file):
        if text_from_file[index].isdigit():
            count += text_from_file[index]
            index+=1
        elif count == '':
            compr_text += text_from_file[index]
            index += 1
        else:
            compr_text += text_from_file[index] * int(count)
            count = ''
            index += 1
    return compr_text

print(recompression_RLE_to_text())