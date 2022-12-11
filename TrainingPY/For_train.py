# a = int(input())
# b = int(input())
#
# for i in range(a,b+1):
#     if i%3 ==0 and i%5==0:
#         print('FizzBuzz')
#     elif i%3==0:
#         print('Fizz')
#     elif i%5==0:
#         print('Buzz')
#     else:
#         print(i)
#
# a = int(input())
# b = int(input())
#
# for i in range(a,b+1):
#     print(f'Число {i}; его квадрат = {i**2}; его куб = {i**3}')

# summ = 0
#
# for i in range(50,101):
#         summ += i**3
# print(summ)
#
# n = int(input())
# summ = 1
# if n==1 or n==0:
#     summ=1
# else:
#     for i in range(1,n+1):
#         summ *=i
# print(summ)
#
#
# n=int(input())
# a=0
# b=0
# for i in range(n):
#     m, c = map(int,input().split())
#     a+=m
#     b+=c
# if a>b:
#     print('Mishka')
# elif a<b:
#     print('Chris')
# elif a == b:
#     print('Friendship is magic!^^')
#
# n=int(input())
# count=0
# for i in range(n):
#     text =input().lower()
#     if 'рок' in text:
#         num = text.find('рок')
#         print(f'{i+1} {num+1}')
#     else:
#         pass
#
# n=int(input())
# count=0
# accum = ''
# for i in range(n):
#     recept =input().lower()
#     if 'соль' not in recept:
#         accum += recept +', '
#     else:
#         pass
# print
#
#
#
# n=int(input())
# accum = ''
# num= ''
# for i in range(n):
#     word =input().lower()
#     if len(word)<=10:
#         print(word)
#     else:
#         fir = word[0]
#         num = str(len(word[1:-1]))
#         sec = word[-1]
#         print(fir+num+sec)
# #
# # a = [1, 2, 3, 4, 32, 4, 5, 3, 5]
# # b = []
# # for i in a:
# #     if i not in b:
# #         b.append(i)
# # print(b)
#
# numbers = [-35, 68, -91, 23, -92, -82, -74, 32, 39, -30, -100, -29, 54, 26, 54, -45, 20, 53, -17, 68, -35, 11, 26, -17, 70, 89, -81, -4, 61, -45, 13, 63, -48, -66, -92, -15, -88, -87, -75, 44, -49, -81, 19, -33, -59, 85, -69, -60, 9, -98, 28, 11, 15, -35, -80, 5, -20, -52, -45, 26, 47, -16, 40, -14, -12, 15, 73, -16, 29, -98, 93, -77, 1, 85, 77, 73, 100, -71, 99, 39, 2, -38, 49, -31, 15, 43, 94, -39, -89, -46, -71, 39, -56, 41, -93, 4, -79, 48, 88, -51]
# for i in range(len(numbers)): #если используем индексы в начале цикла обязательно пишем Range
#     numbers[i] = numbers[i]*2
# print(numbers)
#
# n = int(input())
# listok = []
# for i in range(n):
#     text = input()
#     listok.append(text)
#
# print(listok)
#
# char = input()
# text = input().split()
# for i in range(len(text)):
#     if char in text[i]:
#         print(text[i])

# numbers = list(map(int, input().split()))
# num = int(input())
# for i in range(len(numbers)):
#     if num == numbers[i]:
#         print(i+1)
#         break
# else:
#      print('ErrorValue')
#
# numbers = list(map(int, input().split()))
# num = []
# for i in range(len(numbers)-1):
#     if numbers[i]>0:
#         num.append(numbers[i])
#     print(min(num))
# else:
#     if len(num) == 0:
#         print('Empty')
#     else:
#         print(min(num))
#
# num = input()
# sum_even = 0
# sum_odd = 0
# for i in range(len(num)):
#     if i % 2 == 0:
#         sum_even += int(num[i])
#     else:
#         sum_odd += int(num[i])
# else:
#     if(sum_even-sum_odd)%11 == 0:
#         print('YES')
#     else:
#         print('NO')
#
# num = input()
# count = 0
# summ = 0
# for i in range(len(num)):
#     if num[i].isdigit():
#         summ += int(num[i])
#         count +=1
# else:
#     print(f'{count} {summ}')

# text = input()
# new = []
# for i in range(len(text)):
#     if text.count("(") == text.count(")") or len(text) == 0:
#         pass
#
#         for k in range(i + 1, len(text)):
#             if text[i] == text[k]:
#                 break
#             else:
#                 pass
#     elif text[0] == ')':
#         break
#     else:
#         break
# else:
#     if len(text) == 0:
#         print("YES")
#     else:
#         print("YES")


# Правильная скобочная последовательность
# text = input()
# new = []
# fir = -1
# chek = True
# for i in range(len(text)):
#     if chek == True:
#         if text.count("(") == text.count(")") and text[0] != ')' and text[-1] != '(' :
#             pass
#             for k in range(i+1,len(text)):
#                 if text[i] == text[k]:
#                     fir+=-1
#                 else:
#                     fir+=1
#             else:
#                 chek = False
#                 break
#         else: break
#     else:
#         break
#
# if len(text) == 0 or fir == 0 :
#     print("YES")
# else:
#     print("NO")

#Продвинутый поиск скобочек

import sys
text = input()
new = []
crug = -1
kvad = -1
fig = -1
chek = True
fish = 0
p = 0
for i in range(p,len(text)):
    if chek ==True:
        if (text.count("(") == text.count(")") and text[0] != ')' and text[-1] != '(') \
                and (text.count("[") == text.count("]") and text[0] != ']' and text[-1] != '[') \
                and (text.count("{") == text.count("}") and text[0] != '}' and text[-1] != '{'):
            for k in range(i+1,len(text)):
                crug = -1
                kvad = -1
                fig = -1
                if text[i] == '(':
                    if text[i+1] == ']' or text[i+1] == '}':
                        chek = False
                        break
                    elif text[i] == text[k]:
                        crug -= 1
                    elif text[k] == ')':
                        crug +=1
                elif text[i] == '[':
                    if text[i+1] == ')' or text[i+1] == '}':
                        chek = False
                        break
                    elif text[i] == text[k]:
                        kvad -= 1
                    elif text[k] == ']':
                        kvad += 1
                elif text[i] == '{':
                    if text[i+1] == ')' or text[i+1] == ']':
                        chek = False
                        break
                    elif text[i] == text[k]:
                        fig -= 1
                    elif text[k] == '}':
                        fig += 1
        else:
            fish = 1
            break
    else:
        fish = 1
        break

if fish ==1:
    print("NO")
elif len(text) == 0 or crug == 0 and kvad == 0 and fig == 0:
    print("YES")
elif (crug == -1 and kvad == 0 and fig == 0) or (crug == 0 and kvad == -1 and  fig == 0):
    print("YES")
elif (crug == 0 and kvad == 0 and fig == -1) or ((crug == -1 and kvad == 0 and fig == -1)):
    print("YES")
elif (crug == 0 and kvad == -1 and fig == -1) or ((crug == -1 and kvad == -1 and fig == 0)):
    print("YES")
else:
    print("NO")

#
# # Второй вариант решения
# a=str(input())
# b=[]
# for i in a:
#     if len(b)==0:
#         b.append(i)
#     else:
#         if b[len(b)-1]=='[' and i==']':
#             b.pop(len(b)-1)
#             continue
#         if b[len(b)-1]=='{' and i=='}':
#             b.pop(len(b)-1)
#             continue
#         if b[len(b)-1]=='(' and i==')':
#             b.pop(len(b)-1)
#             continue
#         b.append(i)
# if len(b)==0:
#     print('YES')
# else:
#     print('NO')
#
#
#
# x = list(map(str, input().split()))
# res = []
# result = []
# for c in x:
#     if c.lower() not in res:
#         res.append(c.lower())
#         result.append(c)
# print(*result)
