sp = [int(input()) for i in range(3)]
sp = list(filter(lambda x: x>0, sp))
print(sum(sp))


x = int(input())
print('YES' if len(str(x)) == 4 and (x%7 == 0 or x%17 == 0) else 'NO')


sp = [int(input()) for i in range(4)]
print('YES' if sp[0] == sp[2] or sp[1] == sp[3] else 'NO')


sp = [int(input()) for i in range(4)]
print('YES' if abs(sp[0] - sp[2]) in (0,1) and abs(sp[1] - sp[3]) in (0,1) else 'NO')


n, k = int(input()), int(input())
print("Don't know" if n == k else 'YES' if k > n else  'NO')


a, b,c= int(input()), int(input()), int(input())
print("Равносторонний" if a==b==c else 'Разносторонний' if a!=b!=c and a!=c else 'Равнобедренный')

a, b, c= int(input()), int(input()), int(input())
print(a if b<a<c or c<a<b else b if a<b<c or c<b<a else c)

a = int(input())
l = [1,3,5,7,8 ,10,12]
print('31' if a in l else '30' if a!= 2 else '28')

a = int(input())
print('Легкий вес' if a < 60 else 'Полусредний вес' if 64<=a<69 else 'Первый полусредний вес')



a, b, op = input(), input(), input()
if op not in ('+', '-', '*', '/'):
    print("Неверная операция")
else:
    print("На ноль делить нельзя!" if op == '/' and b == '0' else eval(a + op + b))


a, b = input(), input()
col = ['красный', 'синий', 'желтый']
if a not in col or b not in col:
    print("ошибка цвета")
elif a==b:
    print(a)
elif (a == col[0] and b == col[1]) or (a == col[1] and b == col[0]):
    print('фиолетовый')
elif (a == col[0] and b == col[2]) or (a == col[2] and b == col[0]):
    print('оранжевый')
else:
    print('зеленый')



a = int(input())
col = ['зеленый', 'черный', 'красный']
if a<0 or a>36:
    print("ошибка ввода")
elif a==0:
    print(col[0])
elif (1<=a<=10 and a%2 == 0) or (19<=a<=28and a%2 == 0) or (11<=a<=18 and a%2 != 0) or (29<=a<=36and a%2 != 0):
    print(col[1])
else:
    print(col[2])


def compare_segments(line_1, line_2):
    # согласно алгоритму поиска нам надо сделать следующее:
    # сначала сравнить первые координаты отрезков и найти максимальное значение
    first_pair=max(line_1[0], line_2[0])
    # далее нам надо сравнить вторые координаты отрезков и найти минимальное
    second_pair=min(line_1[1], line_2[1])
    # теперь выполняем сравнение полученных величин
    # если первая пара меньше второй
    if first_pair < second_pair:
        # то наш результат следующий
        return(first_pair, second_pair)
    # если пары равны, то у нас пересечение это просто точка
    elif first_pair==second_pair:
        return("результат - точка; %s" % first_pair)
    # а если пара "большего" больше пары "меньшего", то
    else:
         return "пустое множество"

sp = [int(input()) for i in range(4)]
print('YES' if (sp[0]+sp[1])%2 == (sp[2]+sp[3])%2 else 'NO')



num = int(input())
d = {'1': 'I', '2': 'II', '3': 'III', '4': 'IV', '5': 'V', '6': 'VI', '7': 'VII', '8': 'VIII', '9': 'IX', '10': 'X'}
if num < 0 or num > 10:
    print('ошибка')
else:
    print(d[str(num)])

#Задачка про слона в шахматах
sp = [int(input()) for i in range(4)]
if sp[0]-sp[2] == sp[1]-sp[3] or  sp[0]+sp[1] == sp[2]+sp[3] :
    print('YES')
else:
    print('NO')

#Задачка про коня в шахм
sp = [int(input()) for i in range(4)]
if (abs(sp[0]-sp[2]) == 1 and abs(sp[1]-sp[3]) == 2) or (abs(sp[1]-sp[3]) == 1 and abs(sp[0]-sp[2]) == 2):
    print('YES')
else:
    print('NO')

#Ход королевы
sp = [int(input()) for i in range(4)]
if (sp[0]-sp[2] == sp[1]-sp[3] or sp[0]+sp[1] == sp[2]+sp[3]) or sp[0] == sp[2] or sp[1] == sp[3]:
    print('YES')
else:
    print('NO')


nym = float(input())
print(5/9*(nym-32))

nym = int(input())
print(nym*10.5 if nym<3 else 21+((nym-2)*4))


a = float(input())
print(a - int(a))


sp = [int(input()) for i in range(3)]
print(*sorted(sp,reverse = True),sep = '\n')


num = list(input())
num = [int (x) for x in num]
a = max(num)
num.remove(a)
b = min(num)
num.remove(b)
print('Число интересное' if a-b ==num[0] else 'Число неинтересное')


sp = [abs(float(input())) for i in range(5)]
print(sum(sp))


sp = [int(input()) for i in range(4)]
print(abs(sp[0]-sp[2]) + abs(sp[1]-sp[3]))


sp = [input() for _ in range(3)]
print(min(sp, key=len))
print(max(sp, key=len))


a,b,c = len(input()),len(input()),len(input())
print('YES' if (2*b-c-a)*(2*c-b-a)*(2*a-b-c) == 0 else 'NO')


a = input()
print('YES' if '@' in a and '.' in a else 'NO')


import math
x1,y1,x2,y2= [float(input()) for _ in range(4)]
print(math.sqrt((x1-x2)**2+(y1-y2)**2))


import math
x = float(input())
print(math.pi*x**2)
print(2*math.pi*x)


import math
a,b = float(input()),float(input())
print((a+b)/2)
print(math.sqrt(a*b))
print(2*a*b/(a+b))
print(math.sqrt((a**2+b**2)/2))



import math
a = float(input())
res1 = math.radians(a)
res2 = (a*math.pi)/180
print(math.sin(res1)+math.cos(res1)+math.tan(res1)**2)



import math
r = []
a,b,c = [float(input()) for _ in range(3)]
res = b**2 - 4*a*c
if res < 0:
    print('Нет корней')
elif res == 0:
    print(-b/(2*a))
else:
    r.append((-b + math.sqrt(res)) / (2*a))
    r.append((-b - math.sqrt(res)) / (2*a))
    print(min(r))
    print(max(r))


import math
n,a= [float(input()) for _ in range(2)]
fir = n*a**2
print(fir/(4*math.tan(math.pi/n)))


n = int(input())
for i in range(n,0,-1):
    print('*'*i)



m,p,n = int(input()),int(input()),int(input())
for i in range(1,n+1):
    print(f'{i} {m}')
    m+=m*(p/100)



m,n = int(input()),int(input())
if m==n:
    print(m)
elif m<n:
    for i in range(m, n+1):
        print(i)
else:
    for i in range(m, n-1,-1):
        print(i)



m,n = int(input()),int(input())
for i in range(m, n+1):
    if i%17==0 or i%10 == 9 or (i%3==0 and i%5==0):
        print(i)


a,b = int(input()),int(input())
count = 0
for i in range(a, b+1):
    if (i**3)%10 == 4 or (i**3)%10 == 9:
        count += 1
print(count)


print(sum([int(input()) for i in range(int(input()))]))



import math
n= int(input())
sp = [1/i for i in range(1,n+1)]
print(sum(sp)-math.log(n))


import math
n = int(input())
sp = [i for i in range(1,n+1) if (i**2)%10 in [2,5,8]]
print(sum(sp))


import math
n = int(input())
factorial = 1
for i in range(1,n+1):
    factorial *=i
print(factorial)



import numpy as np
sp = [int(input()) for i in range(10)]
sp = list(filter(lambda x: x!=0, sp))
print(np.prod(sp))


n = int(input())
tot = 0
for i in range(1,n+1):
    if i%2 == 1:
        tot-=i
    else:
        tot+=i
print(-1*tot)


sp = [int(input()) for i in range(int(input()))]
print(max(sp))
sp.remove(max(sp))
print(max(sp))


f = 'YES'
for _ in range(10):
    if int(input())%2:
        f = 'NO'
print(f)


n = int(input())
if n==1:
    print(1)
    exit()
fib1 = 1
fib2 = 1
print(fib1, fib2, end=' ')
for i in range(2, n):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end=' ')