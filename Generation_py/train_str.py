# методы для обработки строк в Python:
#
# • isalpha(str): если строка в Python включает в себя лишь алфавитные символы, возвращается True;
#
# • islower(str): True возвращается, если строка включает лишь символы в нижнем регистре;
#
# • isupper(str): True, если символы строки в Python находятся в верхнем регистре;
#
# • startswith(str): True, когда строка начинается с подстроки str;
#
# • isdigit(str): True, когда каждый символ строки — цифра;
#
# • endswith(str): True, когда строка в Python заканчивается на подстроку str;
#
# • upper(): строка переводится в верхний регистр;
#
# • lower(): строка переводится в нижний регистр;
#
# • title(): для перевода начальных символов всех слов в строке в верхний регистр;
#
# • capitalize(): для перевода первой буквы самого первого слова строки в верхний регистр;
#
# • lstrip(): из строки в Python удаляются начальные пробелы; • rstrip(): из строки в Python удаляются конечные пробелы;
#
# • strip(): из строки в Python удаляются и начальные, и конечные пробелы;
#
# • rjust(width): когда длина строки меньше, чем параметр width, слева добавляются пробелы, строка выравнивается по правому краю;
#
# • ljust(width): когда длина строки в Python меньше, чем параметр width, справа от неё добавляются пробелы для дополнения значения width, при этом происходит выравнивание строки по левому краю;
#
# • find(str[, start [, end]): происходит возвращение индекса подстроки в строку в Python. В том случае, если подстрока не найдена, выполняется возвращение числа -1;
#
# • center(width): когда длина строки в Python меньше, чем параметр width, слева и справа добавляются пробелы (равномерно) для дополнения значения width, причём происходит выравнивание строки по центру;
#
# • split([delimeter[, num]]): строку в Python разбиваем на подстроки в зависимости от разделителя;
#
# • replace(old, new[, num]): в строке одна подстрока меняется на другую;
#
# • join(strs): строки объединяются в одну строку, между ними вставляется определённый разделитель.

# s = input()
#
# print('YES' if s == s[::-1] else 'NO')
#
# s = input()
# print(len(s))
# print(s*3)
# print(s[0])
# print(s[:3])
# print(s[-3:])
# print(s[::-1])
# print(s[1:-1])
#
#
# s = input()
# print(s[2])
# print(s[-2])
# print(s[:5])
# print(s[:-2])
# print(s[::2])
# print(s[1::2])
# print(s[::-1])
# print(s[::-2])
#
#
# s = input()
# print(s[len(s)//2 + len(s) % 2:] + s[:len(s)//2 + len(s) % 2])
#
#
# s = input().split()
# print('YES' if s[0][0].isupper() and s[1][0].isupper() else 'NO' )
#
#
# s = input()
# count = 0
# for i in s:
#     if i.isalpha() and i.islower():
#         count+=1
# print(count)
#
#
# count = 0
# for i in range(int(input())):
#     if input().count('11')>=3:
#         count+=1
# print(count)
#
#
# a = input()
# print('YES' if a.endswith(('.com', '.ru')) else 'NO')
#
# a = input()
# maxx = 0
# ind = 0
#
# for i in range(len(a)):
#     if a.count(a[i]) >= maxx:
#         maxx = a.count(a[i])
#         ind = i
#
# print(a[ind])
#
#
# a = input()
# fir = a.find('h')
# sec = a.rfind('h')
# print(a[:fir]+a[sec+1:])
#
#
# print(s.format("2010", "10k", "Bitcoin"))
#
#
#
# a,b = int(input()), int(input())
# for i in range (a,b+1):
#     print(chr(i), f'{i:b}', end =' ')
#
#
#
# s = input()
# for i in range (len(s)):
#     print(ord(s[i]), end =' ')
#
#
#
#
# shift = int(input())
# shift
# s = input()
# per = 0
# for i in range (len(s)):
#     per =  ord(s[i])-shift
#     if per < 97:
#         per = ord(s[i])+26-shift
#     print(chr(per), end ='')
#
#
# s = list(input())
# del s[0::3]
# print(*s, sep='')# put your python code here
#
# s = input()
# if s.count('f') == 1:
#     print(-1)
# elif s.count('f') == 0:
#     print(-2)
# else:
#     ind = s.find('f')
#     print(s.find('f', ind + 1))
#
#
# s = input()
# res = ''
# ind1 = s.find('h')
# ind2 = s.rfind('h')
#
# s1 = s[:ind1]
# s2 = s[ind1:ind2+1]
# s3 = s[ind2+1:]
#
# print(s1+s2[::-1]+s3)
#
#
# n = int(input())
# abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# print([abc[i] for i in range(n)])

# numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
# print(len(numbers))
# print(numbers[-1])
# print(numbers[::-1])
# print('YES' if (5 and 17) in numbers else 'NO')
# print(numbers[1:-1])
#
#
# abc = 'abcdefghijklmnopqrstuvwxyz'
# sp = []
# for i in range(26):
#     sp+=[abc[i]*(i+1)]
# print(sp)
#
#
# sp = []
# for i in range(int(input())):
#     sp+=[int(input())**3]
# print(sp)
#
#
# n = int(input())
# sp = []
# for i in range(1,n+1):
#     if n%i == 0:
#         sp+=[i]
# print(sp)
#
# sp = []
# new = []
# n = int(input())
# for i in range(n):
#     sp += [int(input())]
# for i in range(n - 1):
#     new.append(sp[i] + sp[i + 1])
# print(new)
#
#
# sp = []
# n = int(input())
# for i in range(n):
#     sp+=[int(input())]
#
# print(sp[::2])
#


# sp = []
# tex = ''
# n = int(input())
# for i in range(n):
#     sp+=[input()]
# k = int(input())-1
# for i in range(len(sp)):
#     if len(sp[i]) > k:
#         tex+=sp[i][k]
# print(tex)


# numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
# print(*[i**2 for i in numbers])


# numbers = [int(input()) for _ in range(int(input()))]
# print(*numbers, '' ,*[(x + 1) ** 2 for x in numbers], sep='\n')
#
#
# numbers = [input() for _ in range(int(input()))]
# new =[]
# for i in range(len(numbers)):
#     if numbers[i].isalpha() and numbers[i] not in new:
#         new.append(numbers[i])
# print(*new, sep = '\n')
#
#
# numbers = [input() for _ in range(int(input()))]
# sear = input()
# new =[]
# print(*[el for el in numbers if sear.lower() in el.lower()], sep ='\n')
#
#
# numbers = [input() for _ in range(int(input()))]
# sear = [input() for _ in range(int(input()))]
# new = []
# for el in numbers:
#     for s in sear:
#         if s.lower() in el.lower():
#             pass
#         else:
#             break
#     else:
#         new.append(el)
# print(*new, sep ='\n')
#
#
# numbers = [int(input()) for _ in range(int(input()))]
# new1 = []
# new2 = []
# new3 =[]
# for el in numbers:
#     if el < 0:
#         new1.append(el)
#     elif el == 0:
#         new2.append(el)
#     else:
#         new3.append(el)
# new= new1+new2+new3
# print(*new, sep ='\n')
#
#
#
# x = [int(input()) for _ in range(int(input()))]
# print(*[i for i in x if i < 0], *[i for i in x if i == 0], *[i for i in x if i > 0], sep = '\n')
#
#
# a = input().split()
# res = ''
# for i in a:
#     res+=i[0]+'.'
# print(res)
#
#
# a = input().split()
# print(*['+' * int(el) for el in a], sep = '\n')
#
#
# a = input()
# print(input().join(a))


# names = ['Gvido', 'Roman' , 'Timur']
# print(names)
#
# help(list)
#
#
#
#
# nums = list(map(int,input().split()))
# ma = nums.index(max(nums))
# mi = nums.index(min(nums))
# nums[ma],nums[mi] = nums[mi],nums[ma]
# print(*nums)
#
#
# words = input().lower().split()
# print('Общее количество артиклей:',words.count('a')+words.count('an')+words.count('the'))
#
#
#
# co = input().split('#')
# new = ''
# for i in range(int(co[1])):
#     new = input().split('#')
#     print(new[0].rstrip())
#
#
# [print(input().split('#')[0].rstrip()) for _ in range(int(input()[1:]))]
#
#
# palindromes = [i for i in range(100,1000) if str(i) == str(i)[::-1]]
#
# print(palindromes)


# nums = list(input())
# nums = [i for i in nums if i.isdigit()]
# print(''.join(nums))
#
#
# nums = input().split()
# nums = [int(i)**2 for i in nums if int(i)%2 == 0 and int(i)**2%10 != 4]
# print(*nums)
#

# a = [78, -32, 5, 39, 58, -5, -63, 57, 72, 9, 53, -1]
#
# n = len(a)
# maxx = -10*100000
# # реализация алгоритма сортировки выбором
# for i in range(n):
#     for j in range(n):
#         if a[j]>maxx:
#             maxx = a[j]
#     else:
#         x = a.pop(a.index(maxx))
#         a.insert(n-1,x)
#         n -= 1
#         maxx = -10*100000
# print(a)


#Сортировка простыми вставками
# a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6, 8, -2, 99]
# n = len(a)
#
# for i in range(1, n):
#     elem = a[i]  # первый элемент из неотсортированной части списка
#     j = i
#     while j >= 1 and a[j - 1] > elem:
#         a[j], a[j - 1] = a[j - 1], a[j]
#         j -= 1
#
# print(a)
#
# print('Отсортированный список:', a)
#
#
# lst_1 = [int(i) for i in input().split()]
# lst_2 = [int(i) for i in input().split()]
# res = [i+j for i,j in zip(lst_1,lst_2)]
# print(*res)
#
#
# a = list(map(int,input().split()))
# st = ''
# for el in a:
#     st+=str(el)+'+'
#
# print(f'{st.rstrip("+")}={sum(a)}')
#
#
#
# a = input().split('-')
# res = ''
# if len(a) == 4:
#     res = a[1]+a[2]+a[3]
#     if a[0] == '7' and res.isdigit() and len(a[1])==3 and len(a[2])==3 and len(a[3])==4:
#         print('YES')
#     else:
#         print('NO')
# elif len(a) == 3:
#     res = a[0]+a[1]+a[2]
#     if res.isdigit() and len(a[0])==3 and len(a[1])==3 and len(a[2])==4:
#         print('YES')
#     else:
#         print('NO')
# else:
#     print('NO')
#
#
# print(max([len(el) for el in input().split()]))
#
#
# print(*[el[1:]+el[0]+'ки' for el in input().split()])
#

# def draw_box():
#     print('*'*10)
#     for i in range(12):
#         print('*'+ 12 * ' ' + '*')
#     print('*'*10)
#
# draw_box()
#
#
# def print_digit_sum(num):
#     tot = 0
#     num =  list(str(num))
#     for i in num:
#         tot+=int(i)
#     print(tot)
#
# print_digit_sum(num)
#

# def merge(list1, list2):
#     res = list1+ list2
#     res.sort()
#     return res
#
# print(merge([1, 2, 3], [5, 6, 7, 8]))
#

total = []
for i in range(int(input())):
    total += [int(j) for j in input().split()]

print(total)


def quick_merge(list1, list2):
    result = []

    p1 = 0  # указатель на первый элемент списка list1
    p2 = 0  # указатель на первый элемент списка list2

    while p1 < len(list1) and p2 < len(list2):  # пока не закончился хотя бы один список
        if list1[p1] <= list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1

    if p1 < len(list1):  # прицепление остатка
        result += list1[p1:]
    if p2 < len(list2):
        result += list2[p2:]

    return result