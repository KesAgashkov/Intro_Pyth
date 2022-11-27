# def my_substr(string, lenght):
#     lenght += 1
#     i = 0
#     new_string = ''
#     while i < lenght:
#         new_string = new_string + string[i]
#         i+=1
#     return new_string
#
#
# print(my_substr("Нужно dsdsd", 2))

# def is_contains_char (string, char):
#     i = 0
#     while i < len(string):
#         if string[i] == char:
#             return True
#             i += 1
#         else:
#             i += 1
#     return False
#
#
# print(is_contains_char('Hexlet', 'H'))

# def filter_string(string, char):
#     char_low = char.lower()
#     new = ""
#     for i in string:
#         if i == char or i == char_low:
#             new = new + ""
#         else:
#             new = new + i
#     return new.strip()
#
#
# print(filter_string('П Прfd ипя тdsdsь', 'П'))



def count_vowels(str, char):
    count = 0
    for i in str:
        if symbols.is_vowel(str[i]) == char:
            count += 1
    return count
count_vowels('привет', 'и')

# from kit import show_language, say_hello, say_bye
#
# def print_kit():
#     show_language()
#     say_hello()
#     say_bye()

