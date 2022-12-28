# def count_args(*args):
#     return len(args)
#
#
# def check_sum(*args: int):
#     summ= 0
#     for i in args:
#         summ+=i
#     if summ<50:
#         return print('not enough')
#     else:
#         return print('verification passed')
#
#
# def multiply(*args: int):
#     mult = 1
#     for i in args:
#         mult *= i
#     return mult
#
#
# def only_one_positive(*args: int):
#     count = 0
#     for i in args:
#         if i > 0:
#             count += 1
#     return True if count == 1 else False


# def print_goods(*args: str):
#     count = 0
#     j = 1
#     for i in args:
#         try:
#             if i.isalpha():
#                 print(f'{j}. {i}')
#                 j += 1
#                 count += 1
#             else:
#                 continue
#         except:
#             continue
#     else:
#         if count == 0:
#             return print('Нет товаров')
#
#
# print_goods('Состска', 'Сырок', {}, [], 743)

def info_kwargs(**kwargs):
    kwargs = dict(sorted(kwargs.items()))
    for k, v in kwargs.items():
        print(f'{k} = {v}')


def create_actor(**kwargs):
    name ={'name': 'Райан','surname': 'Рейнольдс','age': 46}
    name.update(kwargs)
    return name


