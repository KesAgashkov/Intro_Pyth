# Давайте вспомним как работает обычная функция
#
# def generator():
#
#          return [1,3,4,5]
#
# при вызове функции generator() – нам разом вернется список [1,3,4,5], но функция генератор представляет из себя функцию которая запоминаем на каком обьекте происходила итерация и возвращает элементы по одному.
#
# Чтобы написать такую функцию смотрите ниже:
#
# def generator():
#
#          for i in range(1,6):
#
#                    yield i – yield это ключевое слово для генератора
#
# давайте сохраним функцию в переменную а:
#
# a = generator()
#
# Теперь мы можем обращаться к нашей переменной а (которая хранит функцию генератор) через функцию next
#
# print(next(a)) – такой вызов будет возвращать по одному элементу из указанных в функции range(1,6)
#
# Так как эта функция – генератор. Элементы ее можно обойти только один раз!
#
# Еще раз о ключевом слове yield – Она в буквально смысле замораживает функцию на том месте где она вызывалась и если у вас после нее есть код то он выполнится только при следующем вызове функции:
#
# def sayGenerator():

# Пример
# def gen_squares(n):
#     for i in range(1,n+1):
#         yield i**2

# еще пример
# def gen_fibonacci_numbers(n):
#     a, b = 1, 1
#     for _ in range(1,n+1):
#         yield a
#         a, b = b, a + b

def my_range_gen(start=0, stop=0, step=1):
    if stop == 0 and step == 1:
        stop=start
        start=0
    if start == stop:
        return
    elif start > stop and step > 0:
        return
    elif start < stop and step < 0:
        return
    elif step == 0:
        return
    else:
        preres = abs((start-stop)//step)
        res = [1]*preres
        for i in res:
            yield start
            start += step

for i in my_range_gen(4,8,-1):
    print(i)


# tests = [(5,), (10,), (-5, 10), (30, 300, 1), (0, -10, -2), (0, -10, 5),
#          (20, 10, 3), (1, 10, -2), (4, 8, 2), (8, 5, -1), (100, 300, 13), (10, 30, 3)]
