# # k = 10
# # z = 0
# # while k <= 14:
# #     z = z + k
# #     k += 1
# #
# # num = 195
# # lim = 6785
# # while num<=lim:
# #     if lim%5 == 0:
# #         print(lim)
# #         lim-=1
# #     lim-=1
#
#
# limak, bob = map(int, input().split())
# yers = 0
# while limak <= bob:
#     limak = limak * 3
#     bob = bob * 2
#     yers += 1
#
#
# print(yers)
#
# numbers = [2, 3, 7, 9, 5, 0, 6, 3, 6, 0, 1, 7, 9, 4, 4, 4, 2, 2, 6, 9, 1, 7, 0, 3, 8, 1, 0, 3, 8, 0, 8, 4, 0, 2, 3, 6, 6, 1, 5, 8, 7, 2, 3, 8, 7, 7, 1, 2, 2, 8, 4, 3, 4, 8, 0, 7, 9, 8, 3, 7, 7, 7, 7, 5, 1, 7, 4, 5, 0, 8, 0, 9, 2, 4, 7, 6, 6, 5, 9, 7, 1, 7, 8, 8, 3, 4, 9, 7, 6, 4, 2, 0, 0, 0, 9, 4, 0, 9, 4, 4, 4, 5, 5, 4, 2, 5, 9, 4, 8, 1, 5, 7, 1, 0, 2, 6, 8, 7, 2, 7, 9, 3, 6, 4, 7, 5, 0, 7, 2, 0, 8, 2, 9, 8, 6, 4, 4, 7, 5, 5, 9, 4, 9, 5, 6, 9, 1, 1, 3, 1, 5, 2, 1, 7, 0, 0, 7, 8, 1, 3, 0, 0, 4, 4, 3, 3, 6, 7, 8, 6, 1, 2, 0, 2, 0, 9, 9, 0, 5, 2, 4, 1, 7, 4, 9, 9, 4, 9, 6, 9, 2, 7, 1, 2, 4, 5, 4, 0, 9, 0]
#
# while 4 in numbers:
#     numbers.remove(4)
# print(*numbers)
#
# word = input()
# ind1 = 1
# ind2 = -1
# print(word)
# while len(word)/2> (ind1-1):
#     new = word[ind1:ind2]
#     print(new)
#     ind1+=1
#     ind2-=1
#
# n = int(input())
# start = 1
# res = 0
# while start ** 2 <= n:
#     res = 0
#     res = start ** 2
#     print(res)
#     start += 1
#
# start, end = map(int, input().split())
# day = 0
# while start <= end:
#     start = start+(start*0.15)
#     day+=1
# print(day+1)
#
# socks, period_add_socks = map(int, input().split())
# day = 0
# while socks > 0:
#     day = socks + (
# print(day+1)

#Задача про проклятые носки
# socks, period_add_socks = map(int, input().split())
# chest = socks
# add = 1
# while chest != 0:
#     if add % period_add_socks == 0:
#         add += 1
#     else:
#         chest -= 1
#         add += 1
# print(add - 1)
#

#Задачка про слепленные свечки

# candles, composit_rate = 4,2
# all_time = 0
# rubish = 0
# while candles > 0:
#     candles -= 1
#     rubish += 1
#     all_time += 1
#     if rubish==composit_rate:
#         candles += 1
#         rubish =0
# print(all_time)

#является ли число степенью двойки
# num = int(input())
# step = 0
# res = 0
# while res < num:
#     res = 0
#     res = 2 ** step
#     step += 1
# if res == num:
#     print(step-1)
# else:
#     print('НЕТ')

# #Надругательство над числом
# a=input()
# res = 0
# while int(a[0])!=1 and res<=1000000000:
#     a=int(a[0])*int(a)
#     res = a
#     a=str(a)
# print(a)

# a=int(input())
# b=int(input())
# c=int(input())
# d=int(input())
# e=int(input())
# f=int(input())
# listok = []
# listok.extend((a,b,c,d,e,f))
# index = 0
# res = 0
# while listok[index] != 0:
#     res+=listok[index]
# print(res)

# n = ''
# while True:
#     n = input()
#     if 5<=len(n)<=9:
#         a = n
#         pass
#     else:
#         break
# print(a)

#задача про проклятого медведя решающего задачи

tasks, t_to_home = map(int,input().split())
tas = 5
count = 0
whole_time = 240 - t_to_home
while whole_time>=0:
    whole_time-=tas
    tas+=5
    if whole_time<0:
        break
    if tasks == count:
        break
    count+=1
print(count)


#Задача про парня с кубиками
import sys
cubes =abs(int(input()))
row = 0
res = 0
add = 0
if cubes==0 or cubes==1:
    print(1)
    sys.exit()
else:
    while cubes>0:
        res+=(add+1)
        cubes-=res
        if cubes<0:
            break
        row += 1
        add+=1
print(row)


n,m = map(int,input().split())
fir=list(map(int,input().split()))
sec=list(map(int,input().split()))
listok = fir+sec
lenght = len(listok)
result = []
i = 0
j = 0
minn = listok[0]
while True:
    if minn>listok[i]:
        minn = listok[i]
        i+=1
        j = i-1
    else:
        i+=1
    if i == len(listok):
        result.append(minn)
        listok.pop(j)
        i = 0
        j = 0
        if len(result) == lenght:
            break
        minn = listok[i]
print(*result)


n,m = map(int,input().split())
fir=list(map(int,input().split()))
sec=list(map(int,input().split()))
listok = fir+sec
lenght = len(listok)
result = []
i = 0
minn = listok[0]
while len(result) != lenght:
    a = min(listok)
    b=listok.index(a)
    result.append(min(listok))
    listok.pop(b)
print(*result)


#Проверка числа на простоту
x = int(input())
x1 = x
while x1 > 2:
    x1 -= 1
    if x % x1 == 0:
        print('No')
        break
else:
    if x == 1:
        print('No')
    else:
        print('Yes')

#Нахождение всех делителей числа
x = int(input())
num = 1
res = 0
while num<=x:
    if x%num == 0:
        res= res+num
        num+=1
    else:
        num+=1
print(res)

#Нод 1 метод
a,b = map(int,input().split())

while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a
print(a)

#Нод 2 метод
a,b = map(int,input().split())
while b > 0:
    c = a%b
    a = b
    b = c
print(a)


#Нок поиск
a,b = map(int,input().split())
d = a*b
while b > 0:
    c = a%b
    a = b
    b = c
print(int(d/a))

num = int(input())
count = 2
while True:
    if num%count == 0:
        break
    count+=1
print(count)


num1 = int(input())
num2 = int(input())
while num1<=num2:
    if num1==777:
        break
    elif num1%2 == 0 or num1%3 == 0:
        num1+=1
        continue
    print(num1)
    num1+=1

#Сиракузская последовательность
num = int(input())
count=0
while True:
    if num == 1:
        break
    elif num%2==0:
        num/=2
        count+=1
    else:
        num = 3*num+1
        count+=1
print(count)

text = list(input())
i = 0
while i< len(text):
    if text[i] == 'e' or text[i] == 'a':
        print('Ага! Нашлась')
        break
    else:
        print (f'Текущая буква: {text[i]}')
        i+=1
else:print('Распечатали все буквы') #Крутое дополнение которое, выполняется сразу после окончания цикла



