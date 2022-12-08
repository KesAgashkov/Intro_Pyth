# 1. Напишите программу, удаляющую из текста все слова, содержащие заданную строку.
#
# Пример:
# Пугать ты галок пугай => заданная строка "галок" => Пугать ты пугай
# Пугать ты галок пугай => заданная строка "пуг" => Пугать ты галок
#
def search_substr(input_text: str, substr: str)->str:
    """
       Функция фильтрует слова в строке по наличию в них указанного элемента

       Args:
           input_text: str
           substr: str
       Returns:
           new_text - обновленная строка
    """
    input_text = list(input_text.split())
    new_text = []
    for item in input_text:
        if substr in item:
            pass
        else:
            new_text.append(item)
    return new_text

# print(*search_substr('Пугать ты галок пугай', "у"))

# 2. Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021(или сколько вы скажете) конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28
# (или сколько вы зададите в начале) конфет. Все конфеты оппонента достаются сделавшему последний ход.
# Сделайте эту игру.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
#
# Если делаете a и b - не нужно создавать отдельных файлов с полностью копированным кодом,
# лучше выделите в отдельные функции бота и умного бота.

from random import randint
import sys
import time

def game_candles():
    """
       Функция реализует игру про конфеты

       Returns:
           str - строка с указанием победителя
    """
count_candyes =  int(input('        Добро пожаловать в игру\n\nВведите количество конфет в начале игры: \n'))
max_get = int(input("Укажите количество максимальное количество конфет\nкоторое может взять игрок за один раз: \n"))
count = 0
if count_candyes < max_get:
    print('Количество конфет не может быть меньше максимального количества конфет, которое можно взять.\n Пробуйте еще раз')
    game_candles()
cheet = (count_candyes % max_get)-1
def bot_for_game(): #Ботяра (тупенький)
    if max_get<count_candyes:
        bot = randint(1,max_get)
    else:
        bot = randint(1, count_candyes)
    return bot

def bot_for_game_improve(): #Ботяра 2(относительно умный)
    if count == 0 and count_candyes == max_get:
        bot = count_candyes
    elif cheet == -1 and count == 0:
        bot = 1
    elif count == 0:
        bot = cheet
    elif sec==max_get:
        bot = max_get
    elif count_candyes<=max_get:
        bot = count_candyes
    else:
        bot = max_get - sec
    return bot

mode = int(input('Выбери режим игры: \n1: 1 на 1\n2: Против тупого бота\n3: Против умного бота\n'))
game_candles() if mode != 1 or mode != 2 or mode != 3 else None
if mode == 1:
    print('Киньте монетку, чтобы определить очередность или выберите число от 1 до 2: \n')
    time.sleep(5)
    print('Готовы?\n')
    time.sleep(2)
    print(randint(1,2))

    print('Кто угадал число, тот и будет первым игроком\n')

    time.sleep(3)

print(f'''На столе лежит {count_candyes} конфет(a,ы).
Играют два игрока делая ход друг после друга.
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем {max_get} конфет.
Все конфеты оппонента достаются сделавшему последний ход.
''')

time.sleep(6)
if mode == 1:
    print("""Пссс,Парень хочешь научу тебя выигрывать всегда, не будешь знать куда конфеты девать???
Просто напиши 'Да' или 'Нет'""")
    res = input().lower()
    if res == 'да':
        print('Мотай на ус!\n Для заданных условий расклад такой!')
        print(f"""Берешь первым ходом {cheet} конфет(ы), а дальше смотришь сколько взял твой противник
    бери следующим ходом столько конфет, чтобы общая сумма была {max_get} и повтори пока не победишь
    """)
    elif res == 'нет':
        print('Честность не порок!\n  Удачи в игре\n')
    else:
        print('Что ты там промямлил???\nБудем считать, что "Да"\n')
        print(f"""Берешь первым ходом {cheet} конфет(ы), а дальше смотришь сколько взял твой противник
    бери следующим ходом столько конфет, чтобы общая сумма была {max_get} и повтори пока не победишь
    """)
print('Все готовы к бойне? Поехали!!!\n')
time.sleep(2)
while True:
    fishka = 1
    if mode ==1:
        fir = int(input(f'Первый игрок. Сколько конфет ты хочешь взять? Нельзя взять больше {max_get} '
                f'и того что осталось {count_candyes}: '))
    else:
        print('Первый игрок сейчас подумает и сделает свой ход')
        time.sleep(3)
    if mode == 2:
        fir = bot_for_game()
    elif mode == 3:
        fir = bot_for_game_improve()

    print(f'Первый игрок взял {fir} конфет\n')
    if fir > max_get or fir > max_get > count_candyes or fir<0 :
        print('Играй честно!!!')
        continue
    else:
        count_candyes -= fir
        print(f'Осталось еще {count_candyes}\n')
        count+=1
        if count_candyes<=0:
            break
    while True:
        fishka = 2
        sec = int(input(f'Второй игрок. Сколько конфет ты хочешь взять? Нельзя взять больше {max_get} и того что осталось {count_candyes}: '))
        if sec > max_get or sec > max_get > count_candyes:
            print('Играй честно!!!')
            continue
        else:
            count_candyes -= sec
            print(f'Осталось еще {count_candyes}\n')
            if count_candyes <= 0:
                break
        break
    if count_candyes <= 0:
        break
print('\nМои поздравления первому игроку,все конфеты твои!\n') if fishka == 1 else print('\nМои поздравления второму игроку,все конфеты твои!\n')
print(f"Игра окончена\n\nМожет ещё одну каточку?\nПросто напиши 'Да' или 'Нет'")

res1 = input().lower() #Почему
game_candles() if res1 == "да" else sys.exit()


game_candles()

#Извне не получилось использовать функцию, почему, и как это можно решить

# 3. Создайте программу для игры в ""Крестики-нолики"".

def game_cross_zero():
    area = [
        ['*', '*', '*'],
        ['*', '*', '*'],
        ['*', '*', '*']
    ]
    print('Добро пожаловать в игру "Крестики-Нолики"')
    print('Киньте монетку, чтобы определить очередность или выберите число от 1 до 2: \n')
    time.sleep(1)
    print('Готовы?\n')
    time.sleep(2)
    print(f'       {randint(1,2)}\n')
    for item in area:
        print(f'{item}\n')

    while True:
        fir1, fir2 = map(int, input('Первый игрок. Напиши номер строки и столбца через пробел (1-3),'
                                    'где хочешь поставить "X"(Счёт идёт с левого верхнего угла):').split())
        fir1 = int(fir1 - 1)
        fir2 = int(fir2 - 1)
        if fir1 in [0, 1, 2] and fir2 in [0, 1, 2] and area[fir1][fir2] != "X" and area[fir1][fir2] != "0":
            area[fir1][fir2] = "X"
            for item in area:
                print(f'{item}\n')
        else:
            print('Вы ввели неверные значения, попробуйте заново')
            continue
        if (area[0][0] == 'X' and area[0][1] == 'X' and area[0][2] == 'X') or \
                (area[1][0] == 'X' and area[1][1] == 'X' and area[1][2] == 'X') or \
                (area[2][0] == 'X' and area[2][1] == 'X' and area[2][2] == 'X') or \
                (area[0][0] == 'X' and area[1][0] == 'X' and area[2][0] == 'X') or \
                (area[0][1] == 'X' and area[1][1] == 'X' and area[2][1] == 'X') or \
                (area[0][2] == 'X' and area[1][2] == 'X' and area[2][2] == 'X') or \
                (area[0][0] == 'X' and area[1][1] == 'X' and area[2][2] == 'X') or \
                (area[0][2] == 'X' and area[1][1] == 'X' and area[3][0] == 'X'):
            str1 = 'Победил Первый игрок. Поздравляю'
            return str1
            break

        sec1, sec2 = map(int, input('Второй игрок. Напиши номер строки и столбца через пробел (1-3),'
                                        'где хочешь поставить "0"(Счёт идёт с левого верхнего угла):').split())
        sec1 = int(sec1 - 1)
        sec2 = int(sec2 - 1)
        if sec1 in [0, 1, 2] and sec2 in [0, 1, 2] and area[sec1][sec2] != "X" and area[sec1][sec2] != "0":
            area[sec1][sec2] = "0"
            for item in area:
                print(f'{item}\n')
        if (area[0][0] == '0' and area[0][1] == '0' and area[0][2] == '0') or \
                (area[1][0] == '0' and area[1][1] == '0' and area[1][2] == '0') or \
                (area[2][0] == '0' and area[2][1] == '0' and area[2][2] == '0') or \
                (area[0][0] == '0' and area[1][0] == '0' and area[2][0] == '0') or \
                (area[0][1] == '0' and area[1][1] == '0' and area[2][1] == '0') or \
                (area[0][2] == '0' and area[1][2] == '0' and area[2][2] == '0') or \
                (area[0][0] == '0' and area[1][1] == '0' and area[2][2] == '0') or \
                (area[0][2] == '0' and area[1][1] == '0' and area[3][0] == '0'):
            str2 = 'Победил Второй игрок. Поздравляю'
            return str2
        else:
            print('Вы ввели неверные значения, ход переходит сопернику')
            continue

# Как красиво выйти из двух циклов, ну или хоть как-то?
# print(game_cross_zero())