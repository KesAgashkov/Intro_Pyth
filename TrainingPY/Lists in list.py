# #Поиск суммы диагонали
# n = int(input())
# a = []
# summ = 0
# for i in range(n):
#     a.append(list(map(int,input().split())))
# for i in range(n):
#     for j in range(n):
#         if i==j:
#             summ+=a[i][i]
# print(summ)
#
# #Поменяли в матрице строки на столбцы
# n = int(input())
# a = []
# summ = 0
# for i in range(n):
#     a.append(list(map(int,input().split())))
# for i in range(n):
#     for j in range(n):
#         print(a[j][i], end=' ')
#     print()
#
# #Запись матрицы снизу вверх справа налево
# n = int(input())
# a = []
# summ = 0
# for i in range(n):
#     a.append(list(map(int,input().split())))
# for i in range(n-1,-1,-1):
#     for j in range(n-1,-1,-1):
#         print(a[j][i], end=' ')
#     print()


# Sample Input 1:
#
# 3 4
# 5 9 2 6
# 6 2 4 3
# 1 2 8 7
# Sample Output 1:
#
# 6 2 9 5
# 3 4 2 6
# 7 8 2 1
# n, m = map(int, input().split())
#
# a = []
# summ = 0
# for i in range(n):
#     a.append(list(map(int, input().split())))
# for i in range(n):
#     for j in range(m - 1, -1, -1):
#         print(a[i][j], end=' ')
#     print()


# Sample Input 1:
#
# 3 4
# 5 9 2 6
# 6 2 4 3
# 1 2 8 7
# Sample Output 1:
#
# 1 2 8 7
# 6 2 4 3
# 5 9 2 6

# n, m = map(int, input().split())
# a = []
# for i in range(n):
#     a.append(list(map(int, input().split())))
# for i in range(n - 1, -1, -1):
#     for j in range(m):
#         print(a[i][j], end=' ')
#     print()


# Перед Вами матрица размера 5 × 5, состоящая из 24-x нулей и единственной единицы.
# Строки матрицы пронумеруем числами от 1 до 5 сверху вниз, столбцы матрицы пронумеруем
# числами от 1 до 5 слева направо. За один ход разрешается применить к матрице одно
# из двух следующих преобразований:
#
# Поменять местами две соседние строки матрицы, то есть строки с номерами i и i + 1
# для некоторого целого i (1 ≤ i < 5).
# Поменять местами два соседних столбца матрицы, то есть столбцы с номерами j и j + 1
# для некоторого целого j (1 ≤ j < 5).
# Вы считаете, что матрица будет выглядеть красиво, если единственная единица этой матрицы
# будет находиться в ее центре (в клетке, которая находится на пересечении третьей строки и третьего столбца).
# Посчитайте, какое минимальное количество ходов потребуется, чтобы сделать матрицу красивой.

#Сумма элементов по строкам и по столбцам
# a = []
# x, y = 0, 0
# for i in range(5):
#     a.append(list(map(int, input().split())))
# for i in range(5):
#     for j in range(5):
#         if a[i][j] == 1:
#             x, y = i, j
#             break
# print(abs(x - 2) + abs(y - 2))
#
# n, m = map(int, input().split())
# a = []
# summ_row = 0
# summ_column = 0
# for i in range(n):
#     a.append(list(map(int, input().split())))
# for i in range(n):
#     for j in range(m):
#         summ_row += a[i][j]
#     print(summ_row, end=' ')
#     summ_row = 0
# print()
# for j in range(m):
#     for i in range(n):
#         summ_column += a[i][j]
#     print(summ_column, end=' ')
#     summ_column = 0
#
# #Проверка матрицы на симетрию по главной диагонали
# n = int(input())
# a=[]
# res = ''
# for i in range(n):
#     a.append(list(map(int, input().split())))
# for i in range(n):
#     if res == 'No':
#         break
#     for j in range(n):
#         if a[i][j] != a[j][i]:
#             res = 'No'
#             break
#         else:
#             res = 'Yes'
#
# print(res)
#
# a,b=map(int,input().split())
# s=[]
# q=[]
# for i in range(a):
#     s.append(list(map(int,input().split())))
# for i in range(a):
#         q.append(sum(s[i]))
# print(max(q))
# print(q.index(max(q)))
#
#
#
#
# a,b=map(int,input().split())
# s=[]
# q=[]
# fish = True
# for i in range(a):
#     s.append(list(map(int,input().split())))
# for i in range(a):
#     q.append(max(s[i]))
#     maxx =max(q)
# for j in range(a):
#     if fish==True:
#         for k in range(b):
#             if s[j][k] == maxx:
#                 fish = False
#                 break
#     else:
#         break
# print(max(q))
# print(j-1 , k)
#
# a, b = map(int, input().split())
# s = []
# maxx = []
# summ = []
#
# fish = True
# for i in range(a):
#     s.append(list(map(int, input().split())))
# for i in range(a):
#     maxx.append(max(s[i]))
#     summ.append(sum(s[i]))
# ma = max(maxx)
# champ_ind_1 = maxx.index(max(maxx))
#
#
#
# final = []
# for i in range(a):
#     if ma != maxx[i]:
#         winner = champ_ind_1
#     else:
#         final.append(summ[i])
#
# for j in range(len(final)):
#     if final[j] == max(final):
#         winner = j
#     else:
#         winner = final.index(max(final))
#
# print(winner)
#
#
#
# a, b = map(int, input().split())
# s = []
# maxx = []
# summ = []
#
# fish = True
# for i in range(a):
#     s.append(list(map(int, input().split())))
# for i in range(a):
#     maxx.append(max(s[i]))
# ma = max(maxx)
# print(maxx.count(ma))
#
#
#
# a=[]
# for i in range(4):
#     a.append(input())
# if a[0][0] == a[0][1] == a[1][0] == a[1][1] or a[0][2] == a[0][3] == a[1][2] == a[1][3] or a[2][0] == a[2][1] == a[3][0] == a[3][1] or a[2][2] == a[2][3] == a[3][2] == a[3][3]:
#     print('No')
#
# n, m = map(int, input().split())
# orig = []
# mih = []
# count = 0
# for i in range(n):
#     orig.append(input())
#
# for j in range(n + 1):
#     mih.append(input())
#
# mih.pop(0)
#
#
# n, x = map(int, input().split())
# count = 0
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if i * j == x:
#             count += 1
# print(count)
#
#
# n=int(input())
# a = []
# count = 0
# for i in range(n):
#     a.append(list(map(int,input().split())))
# for i in range(n-1):
#     for j in range(n):
#          if a[j][1] == a[i][0]:
#             count+=1
# count = 5 if count ==4 else count
# print(count)

#
# # Морской бой
# n, m= map(int,input().split())
# a = []
# count = 0
# for i in range(n):
#     a.append(f".{input()}.")
# a = ['......'] + a + ['......']
# for i in range(1,n+1):
#     for j in range(1,m+1):
#          if a[i][j] == '.' and a [i][j+1] == '.' and a [i+1][j] == '.' and a [i][j-1] == '.' and a [i-1][j] == '.':
#             count+=1
#
# print(count)
#
#
# #Заполнение матрицы змейкой
# n, m= map(int,input().split())
# A = []
# B = []
# kof = 0
# for i in range(1,n+1):
#     for j in range((kof*m), n*m):
#         A.append(j)
#         if j>(m*i)-2:
#             if kof%2 != 0:
#                 A = A[::-1]
#             else:
#                 pass
#             B.append(A)
#             A = []
#             kof+=1
#             break
#
# for i in B:
#     print(*i)
#
# #Проверка картинки на то чб или цветная
# n, m = map(int, input().split())
# orig = []
# fish = True
# for i in range(n):
#     orig.append(input().split())
# text = ''
# for i in range(n):
#     if fish == True:
#         for j in range(m):
#             if orig[i][j] == 'C' or orig[i][j] == 'M' or orig[i][j] == 'Y':
#                 text = '#Color'
#                 fish = False
#                 break
#             else:
#                 text = '#Black&White'
#     else:
#         break
#
# print(text)

#Корявый вариант заполнения матрицы змейкой. подходит только для 3 на 3 и пять на пять
# n = 6
# p = [[0] * n]
# j = 1
# koef_1 = 1
# koef_2 = 2
# flag=True
# m = 0
# for el in range(n - 1):
#     p.append([0] * n)
# while m != n * n:
#     if m == n * n-1:
#         break
#     else:
#         for i in range(0, n):
#             p[0][i] = i + 1
#             m = i + 2
#         while j < n:
#             p[j][i] = m
#             j += 1
#             m += 1
#         if m == n * n:
#             break
#
#         j = n - 2
#         i = n - 1
#         while j > -1:
#             p[i][j] = m
#             j -= 1
#             m += 1
#             if m == n * n:
#                 break
#         j = 0
#         i = n - 2
#         while i > 0:
#             p[i][j] = m
#             i -= 1
#             m += 1
#         if m == (n * n) - 1:
#             break
#
#         j = n - 4
#         i = (n - n) + 1
#         if m >= n * n - 1:
#             flag = False
#             break
#         while j < n - 1:
#             p[i][j] = m
#             j += 1
#             m += 1
#             if m == n * n-1:
#                 break
#         j = n - 2
#         i = n - 3
#         while i < n-1:
#             p[i][j] = m
#             i += 1
#             m += 1
#         if m == n * n:
#             break
#
#         j = n - 3
#         i = n - 2
#         while j > 0:
#             p[i][j] = m
#             j -= 1
#             m += 1
#         if m == n * n:
#             break
#
#         j = n - 4
#         i = n - 3
#         while i > n-4:
#             p[i][j] = m
#             i -= 1
#             m += 1
#         if m == n * n:
#             break
#
# p[int(n/2)][int(n/2)] = n**2
#
# for i in p:
#     print(*i)

# #Хороший вариант
# n = 4
# # int(input())
# p = [[0] * n for el in range(n)]
# i = 1
# x = 0
# y = -1
# d_row = 0
# d_col = 1
# lenght = len(str(n**2))
# while i <= n ** 2:
#     if 0 <= x + d_row < n and 0 <= y + d_col < n and (p[x + d_row][y + d_col]) == 0:
#         x += d_row
#         y += d_col
#         p[x][y] = i
#         i += 1
#     else:
#         if d_col == 1:
#             d_col = 0
#             d_row = 1
#         elif d_row == 1:
#             d_row = 0
#             d_col = -1
#         elif d_col == -1:
#             d_col = 0
#             d_row = -1
#         elif d_row == -1:
#             d_row = 0
#             d_col = 1
#
# for i in p:
#     for j in i:
#         print(str(j).rjust(lenght), end = ' ')
#     print()

r, c = 3,4
# map(int, input().split())
orig = []
count_row = 0
count_col = 0

orig = [['S...'],['....'],['..S.']]
# for i in range(r):
#     orig.append(input().split())
for i in range(r):
    if 'S' in orig[i][0]:
        pass
    else:
        count_row += 1

for i in range(r):
    for j in range(c):
        if 'S' in orig[i[j]]:
            break
    else:
        count_col += 1


#Лютая задача про поедателя тортов 
r, c = map(int, input().split())
orig = []
count_row = 0
count_col = 0
for i in range(r):
    orig.append(input())

for item in range(r):
    if 'S' in orig[item]:
        pass
    else:
        count_row += 1

for j in range(c):
    for i in range(r):
        if orig[i][j] == 'S':
            break
    else:
        count_col += 1

res = (c * count_row) + (r - count_row) * count_col

print(res)
