def print_from(n: int) -> None:
    if n == 0:
        return
    print(n)
    print_from(n - 1)


def my_sort(n,listok):
    if n > 0:
        print(listok[n-1],end = ' ')
        my_sort(n-1,listok)

n = int(input())
listok = list(map(int,input().split()))
my_sort(n,listok)



def double_fact(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    if n>=2:
        f = n * double_fact(n - 2)
        return f



def fib(n):
    f1 = 0
    f2 = 0
    f3 = 1

    list_1 = []
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 0
    for _ in range(1,n+2):
        list_1.append(f1)
        f1,f2 = f2, f1 + f2
    return list_1[-1]
n = int(input())
print(fib(n))


def tribonacci(n):
    f1 = 0
    f2 = 0
    f3 = 1
    fib_sum = 0
    list_1 = []
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    for _ in range(n-2):
        fib_sum = f1 + f2 + f3
        f1 = f2
        f2 = f3
        f3 = fib_sum
    return fib_sum


def get_combin(n: int, k:int) -> int:
    if k == n or k == 0:
        return 1
    if k != 1:
        return get_combin(n-1, k) + get_combin(n-1, k-1)
    else:
        return n


def ackermann(m, n):
    if m == 0:
        return n + 1
    if m > 0 and n == 0:
        return ackermann(m - 1, 1)
    if m > 0 and n > 0:
        return ackermann(m - 1, ackermann(m, n - 1))


def flatten(spisok):
    new=[]
    spisok = str(spisok)
    for i in spisok:
        if i.isdigit()  :
            new.append(int(i))
    return new


# строка типа f(h(k(o)s)a

def rec(s):
    if len(s) == 1 or len(s) == 2:
        return s
    return s[0] + '(' + rec(s[1:-1]) + ')' + s[-1]
s = input()
print(rec(s))

# возведение в степень целых чисел (и отрицательных, и положительных)

def power(x, n):
    if n == 0:
        return 1
    if n < 0:
        return 1/power(x, -n)
    if n % 2 == 0:
        return power(x, n//2)*power(x, n//2)
    else:
        return power(x, n-1)*power(x, n-1)

# глубина вложенного списка

a = [1,[3,[2,3,[4]]],2,[2,3,4,[3,4,[2,3],5]]]

def rec(spicok, level=1):
    print(*spicok, 'level=', level)
    for i in spicok:
        if type(i) == list:
            rec(i, level+1)

rec(a)


# Поиск файла
import os

discName = input('Введите букву диска: ') + ':\\'
fileName = input('Введите имя файла для поиска: ')


def search(path):
    for i in os.listdir(path):
        if os.path.isdir(path + '\\' + i):
            search(path + '\\' + i)
        if i == fileName:
            return print(f'Файл находится в директории: {path}')


search(discName)


