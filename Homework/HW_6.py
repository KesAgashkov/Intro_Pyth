# Вам нужно решить задачи с помощью лямбд, filter, map, zip, enumerate, list comprehension
#
# 1- Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

# texts = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
# # list(input().split())
# char = "йцу"
# x = 0
# # input()
# # count = 0
# # for i in range(len(texts)):
# #     if char in texts[i]:
# #         count+=1
# #         if count==2:
# #             break
# # print(i)
#
#
# nums = [n for n in range(len(texts)) if char == texts[n]]
# if len(nums) == 0:
#     x=-1
# elif len(nums) == 1:
#     nums[0]
# else:
#     x = nums[1]
# # print(x)

# odd_squares = [n*n for n in nums if n%2 == 1]
# 2- Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и
# предпоследний и т.д.
#
# nums = list(map(int,input().split()))
# numers = [nums[n]*nums[n-n-(1+n)] for n in range(int(len(nums)/2))]
# print(numers)

#
# 3-Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.
#

# num = int(input())
# numer = [0,1]
# for n in range(1,num):
#     a = numer[n]*-3
#     numer.append(a)
#
# print(numer[1:])

# numers = [numer[n]*-3 for n in range(1, num)]
# print(numer[1:])

# 4 - Дан список URL различных сайтов. Нужно составить список доменных имен сайтов.
#
urls_list = ['https://www.hugedomains.com/domain_profile.cfm?d=litcode.com',
             'https://www.gosuslugi.ru/',
             'https://www.avito.ru/saratov/predlozheniya_uslug/massazh_2675272891',
             'https://gb.ru/',
             'https://pythontutor.ru/visualizer/']
domens_list = []
for i in range(len(urls_list)):
    change = urls_list[i].partition('//')[-1]
    change = change.partition('/')[0]
    domens_list.append(change)
print(*domens_list,sep = "\n")
# 5 - Есть список случайных чисел в промежутке от 1 до 100, количеством 200. Создайте список кортежей,
# первый элемент которого - индекс элемента, а второй - сам элемент, при условии, что они не совпадают.
# 6 - Из списка выше оставьте только те пары, где сумма кортежа кратна 5
# Пример
# [(10,25),(3,4),(4,1)] => [(10,25),(4,1)]

# from random import randint
# numbers = [randint(1,100) for i in range(1,101)]
# indexes = [n for n in range(1,101)]
# res = list(zip(indexes,numbers))
# print(res[1][0])
# res_new_1 = []
# res_new_2 = []
# for i in range(0,len(res)-1):
#     if res[i][0] != res[i][1]:
#         if (res[i][0] + res[i][1]) % 5 == 0:
#             res_new_1.append(res[i][0])
#             res_new_2.append(res[i][1])
# new_res = list(zip(res_new_1,res_new_2))
# print (len(res))
# print (res)
# print(len(new_res))
# print(new_res)

#
# 6 - Из списка выше оставьте только те пары, где сумма кортежа кратна 5
# Пример
# [(10,25),(3,4),(4,1)] => [(10,25),(4,1)]