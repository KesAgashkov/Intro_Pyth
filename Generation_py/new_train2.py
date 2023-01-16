# # a = input()
# # count=0
# # while a not in ('стоп','хватит','достаточно'):
# #     count+=1
# #     a = input()
# # print(count)
# #
# # a = int(input())
# # count=0
# # while a%7==0:
# #     print(a)
# #     a = int(input())
# #
#
# # a = int(input())
# # co=0
# # while -1<a and a<=5:
# #     if a == 5:
# #         co+=1
# #     a = int(input())
# # print(co)
#
# a = 9
# m = 0
# if a >= 25:
#     m = a // 25
#     a = a % 25
# if a >= 10:
#     m += a // 10
#     a = a % 10
# if a >= 5:
#     m += a // 5
#     a = a % 5
# if a < 5:
#     m += a
#
# print(m)
#
#
# reward = int(input())
# total = 0
# for coin in [25, 10, 5, 1]:
#     total += reward // coin
#     reward %= coin
# print(total)
#
#
# num = int(input())
# res = ''
# while num != 0:
#     last_digit = num % 10
#     res+=str(last_digit)
#     num = num // 10
# print(res)
#
#
# num = int(input())
# max = 1
# min = 9
# while num != 0:
#     last_digit = num % 10
#     if last_digit<min:
#         min = last_digit
#     if last_digit>max:
#         max = last_digit
#     num = num // 10
#
# print(f'Максимальная цифра равна {max}')
# print(f'Минимальная цифра равна {min}')
#
#
# num = int(input())
# tot = 0
# co = 0
# mult = 1
# i = []
# while num != 0:
#     last_digit = num % 10
#     tot += last_digit
#     co += 1
#     mult *= last_digit
#     i.append(last_digit)
#     num = num // 10
#
# print(tot, co, mult, tot / co, i[-1], i[0] + i[-1], sep='\n')
#
#
# num = 19454545
# new = num
# co = 0
# while num != 0:
#     co += 1
#     last_digit = num % 10
#     num = num // 10
# print((new // 10**(co-2)%10 if co>3 else new//10%10 if co==3 else new%10))
#
#
# n = int(input())
# max = -1
# min = 10
# while n>0 :
#     num = n%10
#     if num>max:
#         max = num
#     if num<min:
#         min = num
#     n=n//10
# print('YES' if max==min else 'NO')
#

# n = int(input())
# flag = True
# while n>10 :
#     num1 = n%10
#     num2 = n%100//10
#     if num1>num2:
#         flag = False
#     n=n//10
# print('YES' if flag else 'NO')
#
#
# num = int(input())
# p=0
# for i in range(2, num+1):
#     if num % i == 0:
#         p=i
#         break
# print(p)
#
#
# num = int(input())
# for i in range(1,num+1):
#     if 5<=i<=9:
#         continue
#     if 17<=i<=37:
#         continue
#     if 78<=i<=87:
#         continue
#     print(i)
#
#
# count = 0
# p = 1
# for i in range(10):
#     x = int(input())
#     if x >= 0:
#         p*= x
#         count+= 1
# if count > 0:
#     print(count)
#     print(p)
# else:
#     print('NO')
#
#
# n = int(input())
# for i in range(1,n+1):
#     for j in range(1,10):
#         print(f'{i} + {j} = {i+j}')
#     print()
#
#
#
# import math
# n = int(input())
# for i in range(math.ceil(n/2)):
#     for j in range(i+1):
#         print('*',end = '')
#     print()
# for i in range(math.ceil(n/2),0,-1):
#     for j in range(i-1):
#         print('*',end = '')
#     print()
#
#
# import math
# n = int(input())
# for i in range(1,n+1):
#     for j in range(i):
#         print(i,end = '')
#     print()
#
#
# n = int(input())
# for i in range(1,n+1):
#     print(str(i)*i)



# 28n+30k+31m=365.
# total = 0
# for b in range(1, 100):
#     for k in range(1, 100):
#         for t in range(1, 100):
#             if (10*b + 5*k + 0.5*t == 100) and (b + k + t == 100):
#                 print('b =', b ,'k =', k , 't =', t)





# def get_solution():
#     total = 0
#     for a in range(1, 151):
#         for b in range(1, 151):
#             for c in range(1, 151):
#                 for d in range(1, 151):
#                     for e in range(1, 151):
#                         if a ** 5 + b ** 5 + c ** 5 + d ** 5 == e ** 5:
#                             total += 1
#                             print(a, b, c, d, e)
#                             print('a + b + c + d + e =', a + b + c + d + e)
#     print('Общее количество натуральных решений =', total)
#
# get_solution()
#
#
# num = int(input())             # Определение высоты массива
# count = 0                      # Порядковый номер цифры = число в массиве
# for y in range(1, num + 1):    # Первый цикл высоты массива
#     for x in range(y):         # Второй цикл длины массива
#         count += 1             # увеличиваем счетчик
#         print(count, end=' ')  # Вывод текущего числа и в конце пробел
#     print()
#
#
# n = int(input())
# d = 1
# for i in range(1,n+1):
#     for j in range(i):
#         print(j+1,end = '')
#     for k in range(i-1,0,-1):
#         print(k,end = '')
#     print()
#
# a, b = int(input()), int(input())
# res = 0
# pr = 0
# count = maxx = 0
# c = []
# d = []
# for i in range(1, b + 1):
#     count = 0
#     res = 0
#     for j in range(1, i + 1):
#         if i % j == 0:
#             res += j
#             count += 1
#     else:
#         d.append((count, i))
#         c.append(res)
#
# d.sort(reverse=True)
# print(d)
# print(d[0][1], max(c))
#
#
#
# a, b = int(input()), int(input())
# counter = 0 # счетчик подсчета суммы делителей
# number = 1 # число которое будем выводить (минимум 1)
# summa = 0  # тут будет сумма делителей, которую надо будет вывести
# for i in range(a, b + 1):  # проверяем каждое число в [a;b]
#     counter = 0 # обнуляем счетчик для каждого i
#     for j in range(1, i + 1):  # берем по очереди каждый делитель числа от [1 до самого числа]
#         if i % j == 0:  # если число делится на j без остатка, значит j - делитель числа
#             counter += j  # создаем сумму делителей
#     if counter >= summa:  # если сумма делителей больше или равна, чем суммаа делителей предыдущего числа
#         summa = counter  # то counter теперь равно кол-ву делителей этого числа вместо кол-ва предыдущего
#         number = i  # число у которого делителей оказалось больше, теперь равно number
# print(number, summa) # в конце концов, выводим само число (у которого больше делителей) и сумму этих делителей
#
#
# n = int(input())
# count = 0
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if i%j == 0:
#             count+=1
#     else:
#         print(str(i)+(count*'+'))
#         count = 0
#
#
# n = int(input())
# res = 0
# new = 0
# while n>0:
#     res += n%10
#     n//=10
# while res>0:
#     new += res%10
#     if new>9:
#         new-=res%10
#         break
#     res//=10
# print(new )
#
#
#
# n = int(input())
# total = 0
# fact = 1
# for i in range(1,n+1):
#     fact*=i
#     total+=fact
# print(total)
#
#
# a,b = int(input()),int(input())
# flag = True
# if a==1:
#     a=2
# for i in range(a,b+1):
#     flag = True
#     for j in range(2,b):
#         if i%j == 0:
#             if i!=j:
#                 flag = False
#                 continue
#     else:
#         if flag == True:
#             print(i)
#         else:
#             pass
#
#
# # или так
#
# a, b = int(input()), int(input())
# for i in range(max(2, a), b + 1):
#     for j in range(2, int(i ** 0.5 + 1)):
#         if i % j == 0:
#             break
#     else:
#         print(i)
#
#
# n = int(input())
# s = 0
# while n > 0:
#     if n % 2 == 0:
#         s += n % 10
#     n //= 10
# print(s)
#
# n = 8
# count = 0
# maximum = -10 ** 12
# for i in range(8):
#     x = int(input())
#     if x % 4 == 0:
#         count += 1
#         if x > maximum:
#             maximum = x
# if count > 0:
#     print(count)
#     print(maximum)
# else:
#     print('NO')
#
#
# n = int(input())
# for i in range(n):
#     if i==0:
#         print('*'*19)
#     elif i==n-1:
#         print('*'*19)
#     else:
#         print('*'+ 17*' ' + '*')
#
#
# n = int(input())
# p = n
# count = 0
# while n>0:
#     n//=10
#     count+=1
# print(p//10**(count-3)%10)
#
#
# n = int(input())
# p = n
# count3 = 0
# count_last = 0
# count_even = 0
# tot_up5 = 0
# prod_up7 = 1
# count_0_5 = 0
# last = n%10
# while n>0:
#     res = n%10
#     if res == 3:
#         count3+=1
#     if res == last:
#         count_last+=1
#     if res%2 == 0:
#         count_even+=1
#     if res>5:
#         tot_up5+=res
#     if res>7:
#         prod_up7*=res
#     if res==0 or res ==5:
#         count_0_5+=1
#     n//=10
# print(count3,count_last,count_even,tot_up5,prod_up7,count_0_5, sep = '\n')

#
# answer=[]
# for i in range(1, 70):
#     for j in range(1, 70):
#         for x in range(1, 70):
#             for y in range(1, 70):
#                 if i ** 3 + j ** 3 == x ** 3 + y ** 3 and i < x < y < j:
#                     answer.append(x ** 3 + y ** 3)
# print(sorted(answer))

import emoji

a = input()
count = 0
for i in range(len(a) - 1):
    if a[i] == a[i + 1]:
        count += 1
print(count)


