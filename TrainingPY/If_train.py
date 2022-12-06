num_1 = input()
num_2 = input()
num_1 = list(num_1)
char1 = num_1.pop(0)
cif1 = int(num_1.pop(0))
num_2 = list(num_2)
char2 = num_2.pop(0)
cif2 = int(num_2.pop(0))

if char1 == 'a':
    char1 = 1
elif char1 == 'b':
    char1 = 2
elif char1 == 'c':
    char1 = 3
elif char1 == 'd':
    char1 = 4
elif char1 == 'e':
    char1 = 5
elif char1 == 'f':
    char1 = 6
elif char1 == 'g':
    char1 = 7
else:
    char1 = 8

if char2 == 'a':
    char2 = 1
elif char2 == 'b':
    char2 = 2
elif char2 == 'c':
    char2 = 3
elif char2 == 'd':
    char2 = 4
elif char2 == 'e':
    char2 = 5
elif char2 == 'f':
    char2 = 6
elif char2 == 'g':
    char2 = 7
else:
    char2 = 8

if char1 % 2 == 1 and char2 % 2 == 1:

    if (cif1 + cif2) % 2 == 0:
        print('YES')
    else:
        print('NO')

elif char1 % 2 == 0 and char2 % 2 == 0:

    if (cif1 + cif2) % 2 == 0:
        print('YES')
    else:
        print('NO')

else:
    if (cif1 + cif2) % 2 == 1:
        print('YES')
    else:
        print('NO')

s, v1, v2, t1, t2 = map(int,input().split())
first_speed = s*v1+(2*t1)
sec_speed = s*v2+(2*t2)
if first_speed<sec_speed:
    print('First')
elif first_speed>sec_speed:
    print('Second')
else:
    print('Friendship')

fir = input().lower()
sec = input().lower()
if fir[-1] != 'ь':
    if fir[-1] == sec[0]:
        print('Good')
    else:
        print('Bad')
else:
    if fir[-2] == sec[0]:
        print('Good')
    else:
        print('Bad')

x = int(input())
if x%3 == 0 and x%5 == 0:
    print("FizzBuzz")
elif x%3 == 0:
    print("Fizz")
elif x%5 == 0:
    print("Buzz")
else:
    print(x)

month = int(input())
list = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
print(list[month-1])

age = int(input())
print('Младенец') if age<2 else None
print('Малыш') if 2<=age<4 else None
print('Ребенок') if 4<=age<12 else None
print('Подросток') if 12<=age<19 else None
print('Взрослый человек') if 19<=age<65 else None
print('Пожилой человек') if age>=65 else None


x = round(float(input()),1)
y = round(float(input()),1)
sigh = input()
if sigh == '+':
    print(x+y)
elif sigh == '-':
    print(x-y)
elif sigh == '*':
    print(round((x*y),1))
elif sigh == '/':
    if y != 0:
        print(round((x/y),1))
    else:
        print('Неизвестно')
else:
    print('Неизвестно')


fir = input()
sec = input()
if len(fir) < 6:
    print('Short')
elif fir != sec:
    print('Difference')
else:
    print('OK')



course = int(input())

match course:
    case 1:
        print("Совсем еще зеленый студентик")
    case 2:
        print("Джун-студент")

    case 3:
        print("Мидл-студент")

    case 4:
        print("Сеньер-студент")

    case 5:
        print("Босс качалки")
    case  _:
        print("Неизвестный курс")


num_month = int(input())

match course:
    case 1|3|5|7|8|10|12:
        print(31)
    case 4|6|9|11:
        print(30)
    case  _:
        print(28)

num_month = input()

match num_month:
    case 'Овен'|'Лев'|'Стрелец':
        print('Огненный')
    case 'Телец'|'Дева'|'Козерог':
        print('Земной')
    case 'Близнецы'|'Весы'|'Водолей':
        print('Воздушный')
    case  _:
        print('Водный')

# меняйте значение переменной value
value = [1, 2, 3]

match value:
    case int() | float():
        print("Имеем дело с числом")
    case str():
        print("Имеем дело со строкой")
    case list():
        print("Имеем дело со списком")
    case  _:
        print(f"Лучше с этим дел не иметь")


