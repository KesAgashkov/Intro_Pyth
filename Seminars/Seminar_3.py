def give_int(input_string: str,
             min_num: Optional[int] = None,
             max_num: Optional[int] = None) -> int:
    """
    Выпытывает у пользователя число

    Args:
        input_string - предложение ввода
    Returns:
        int - число
    """
    while True:
        try:
            num = int(input(input_string))
            if min_num and num < min_num:
                print(f'Введите больше {min_num}')
                continue
            if max_num and num > max_num:
                print(f'Введите больше, чем {max_num}')
                continue
            return num
        except ValueError:
            print('Вы ввели не число')
# 1. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
# ['gfh5', 'gfh2', '67', 'jy32', '3put'] - ищем 32 - находим по индексу 3

# list_1 = ['gfh5', 'gfh2', '67', 'jy32', '3put']
# for item in list_1:
#     if "32" in item:
#         print(list_1.index(item))

# 2. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
# Пример:
#
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

def search_substr(input_list: list, input_substr: str)->int:
    """
       Ищет индекс элемента с полным совпадением

       Args:
           input_list: list
           input_substr: str
       Returns:
           int - индекс элемента
    """
    for item in input_list:
        if item == input_substr:
            pass
    for i in input_list[1:]:
        if i == input_substr:
            print(f'Индекс искомого элемента: {input_list[1:].index(i)+1}')


search_substr(["qwe","asd", "zxc", "qwe", "ertqwe"], "qwe")


# 3.Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
