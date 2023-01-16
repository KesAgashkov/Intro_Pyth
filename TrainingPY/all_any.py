# Функция all это встроенная функция в которую можно передать аргументом обьект.
#
# Давайте вспомним про логический тип обьекта (bool)
#
# В функцию  bool можно передать обьект, и она вернет True если обьект не является пустым либо нулем.
#
# Например bool(1,2,3,4,’6’) –вернет True ибо эти обьекты являются не пустыми, а bool(0) или bool([]), bool({}) вернут False ибо они являются пустыми.
#
# Функция all также принимает в себя последовательность элементов и возвращает True в случае если все обьекты переданные в эту функцию  не являются пустыми либо нулем:
#
# Давайте создадим список a:
#
# a = ['56', 7, 8.8]
#
# print(all(a))
#
# Вывод: True ибо все элементы внутри списка a являются не пустыми множествами.
#
# Теперь добавим один пустой элемент:
#
#
# a = ['56', 7, 8.8, 0]
#
# print(all(a))
#
# Вывод: False, ибо 0 является пустым множеством, как и пустой список либо кортеж.
#
# Как мы поняли функция all вернет True если переданный в переданном ей аргументе все элементы являются не пустыми, если хотябы один элемент пустой, то вернет False.
#
# Функция any принимает также только один аргумент, но вот только any возвращает True если хотябы один элемент в переданном аргументе является не пустым множеством:
#
# a = [‘’, 0, [], (), 1]
#
# print(any(a))
#
# Вывод: True, так как число 1 является не пустым множеством.
#
# Если убрать его: a = [‘’, 0, [], ()], print(any(a))
#
# Вывод: False ибо все элементы пустые.
#
# Также в эти функции можно передавать свои условные выражения:
#
# a = 13
#
# first = a % 2 == 0 – в данном выражении проверяется четность числа а.
#
# second = a > 11 = проверяем больше ли а чем 11
#
# thirth  = isinstance(a, int) – является ли а инстанцие Int
#
# Теперь можем передавать по одному эти переменные в функции.
#
# Print(all([first])) – выведется False ибо 13 нечетное число
#
# Print(all([second])) – True ибо 13 больше чем 11
#
# Также обратите внимание что мы передаем нашу переменную внутри коллекции, ибо наша переменная вернет булевый тип обьекта а функции all и any такое принять не могут, а вот внутри списка либо кортежа могут.
#
# print(all([first, second, thirth])) – False ибо первое условие не выполняется
#
# print(any([first, second, thirth])) – True ибо выполнются два условия.



# Пример. Во всех ли словах есть буква 'а'
words = list(map(str,input().split()))
print(all(['a' in word.lower() for word in words]))


# и еще один
words = list(map(str,input().split()))
print(any(['ought' == word[-5:].lower() for word in words]))



