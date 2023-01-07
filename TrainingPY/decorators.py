# def text_decor(func):
#     def inner(*args, **kwargs):
#         print('Hello')
#         func(*args, **kwargs)
#         print('Goodbye!')
#
#     return inner
#
# @text_decor
# def simple_func():
#     print('I just simple python func')
# simple_func()


# def repeater(func):
#     def inner(*args, **kwargs):
#         func(*args, **kwargs)
#         func(*args, **kwargs)
#     return inner
#
# @repeater
# def multiply(num1, num2):
#     print(num1 * num2)
#
# multiply(2, 5)


# def double_it(func):
#     def inner(*args, **kwargs):
#         return func(*args, **kwargs) * 2
#     return inner
#
# @double_it
# def multiply(num1, num2):
#     return num1 * num2
#
# res = multiply(9, 4)
# print(res)



import sys
print(sys.getrecursionlimit())


