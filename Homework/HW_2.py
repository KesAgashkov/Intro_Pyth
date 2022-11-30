
# 1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. Учтите, что числа
# могут быть отрицательными
#
# Пример:
#
# 67.82 -> 23
# (-0.56) -> 11


# def summ_el_number_via_string ():
#     num = input("Введите вещественное число (разделитель между цифрами '.'): ")
#     try:
#         num = float(num)
#     except:
#         print('Ошибочка. Попробуйте еще раз')
#         summ_el_number_via_string ()
#     summ = 0
#     num = str(num)
#     num = num.replace('.', '')
#     num = num.replace('-', '')
#     for i in num:
#         summ += int(i)
#     return(summ)
#
# print(summ_el_number_via_string ())
#
# def summ_el_number_via_num ():
#     num = float(input("Введите вещественное число (разделитель между цифрами '.'): "))
#     num = round(num, 10)
#     num = str(num)
#     num = num.replace('-', '')
#     num = num.split(".")
#     num_int = int(num[0])
#     num_fraction = int(num[1])
#     sum_1 = 0
#     sum_2 = 0
#     while num_int>0:
#         sum_1 += int(num_int % 10)
#         num_int /= 10
#     while num_fraction > 0:
#         sum_2 += int(num_fraction % 10)
#         num_fraction /= 10
#
#     return sum_1 + sum_2
#
# print(f'Сумма всех цифр введенного числа равна : {(summ_el_number_via_num ())}')



# 2 - Напишите программу, которая принимает на вход число N и выдает набор произведений (набор - это список)
# чисел от 1 до N.
# Не используйте функцию math.factorial.
#
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] #(1, 1*2, 1*2*3, 1*2*3*4)

def factorial ():
    num = input("Введите натуральное число: ")
    try:
        num = int(num)
    except:
        print('Ошибочка. Попробуйте еще раз')
        factorial()
    if num < 0:
        return 'Ошибочка. Попробуйте еще раз'
    else:
        start = 1
        new_list = []
        i = 0
        result = 1
        while i <= (num-1):
            result = result*(start+i)
            new_list.append(result)
            ## почему нельзя присвоить значения без аппенд по индексу
            i += 1
    return new_list
print(factorial ())
# 3 - Дан массив размера N. После каждого отрицательного элемента массива вставьте элемент с нулевым значением.
#
# Пример:
# - пусть N = 4, тогда [28, -46, 14, -14] => [28, -46, 0, 14, -14, 0]

# def create_list_with_zero ():
#     num = input("Задайте массив целых чисел включая отрицательные числа(для разделения используйте пробел) : ")
#     num = num.split()
#     num = list(num)
#     x = []
#     for i in num:
#         x.append(i)
#         if int(i) < 0:
#             x.append(0)
#     return x

# print(create_list_with_zero())

#
# 4 - По кругу стоят n человек. Ведущий посчитал m человек по кругу, начиная с первого. При этом каждый из тех, кто
# участвовал в этом счете, получил по одной монете, остальные получили по две монеты. Далее человек, на котором
# остановился счет, отдает все свои монеты следующему по счету человеку, а сам выбывает из круга. Процесс продолжается с
# места остановки аналогичным образом до последнего человека в круге. Составьте алгоритм, который проводит эту игру.
# Если хотите делать паузы, то импортируйте библиотеку time и используйте оттуда функцию sleep.
# Определите номер этого человека и количество монет, которые оказались у него в конце игры.

# def game_with_coins (whole_num, choose num):

# whole_num = 5
#
# choose_num = 2
# num_two_coin = whole_num - choose_num
# list_partic = [1] * choose_num + [2] * num_two_coin
# print(list_partic)
# new_partic = []
# k = 0
# p = 0
# x = 0
#
# while k <= whole_num:
#     new_partic.append(list_partic[k])
#     k += 1
#
# new_partic[choose_num] = list_partic[choose_num - 1] + list_partic[choose_num]
# new_partic.pop(choose_num - 1)
# whole_num = whole_num - 1
#
# print(new_partic)
#
# whole_num = whole_num - 1
#
#
# print(new_partic)

# x = 0
# x = list_partic[i]+list_partic[i+1]
# new_partic.append(x)
# # print(new_partic)
# while i > 0:
#     new_partic.append(list_partic[i])
#     i-=1
#
# new_partic.append(list_partic[i])
# x = list_partic[i]+list_partic[i+1]
# new_partic.append(x)




# print(list_poor,f'\n{list_rich}')

