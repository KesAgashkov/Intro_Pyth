my_list = [56, 59, 53, 75, 62, 61, 75, 65, 59, 62, 64, 53,
           54, 62, 69, 53, 55, 62, 54, 66, 55, 57, 58, 75,
           72, 55, 51, 56, 71, 66, 57, 56, 59, 73, 68, 57,
           50, 54, 62, 68, 59, 64, 59, 59, 71, 68, 57, 54, 53, 72]
my_set = set(my_list)
print(sum(my_set) / len(my_set))


text = input()
text = set(text)
if len(text)%2==0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')



spis = list(map(int,input().split()))
fir = len(spis)
sec = len(set(spis))

print(fir-sec)


from string import ascii_lowercase
vvod = input().lower()
vvod = set(vvod)
text= set(ascii_lowercase)
if vvod == text:
    print('YES')
else:
    print('NO')

year = input()
start = int(year) + 1
year = str(start)
check = set(year)
while len(check) != 4:
    start += 1
    check = set(str(start))
print(start)


s = input()
if s == '{}':
    print(0)
else:
    s = s.lstrip('{').rstrip('}').replace(' ', '').split(',')
    s = set(s)
    print(0 if len(s) == 0 else len(s))


set_a = {31, 37, 39, 41, 47, 58, 60, 62, 70, 75,
         76, 77, 78, 79, 80, 81, 85, 86, 88, 90, 93, 96, 98, 99}

set_b = {0, 1, 8, 16, 17, 18, 22, 24, 29, 31,
         33, 34, 36, 42, 46, 47, 51, 53, 62, 64, 65, 66, 67}

res = set_a & set_b
print(len(res))

set_a = {31, 37, 39, 41, 47, 58, 60, 62, 70, 75,
         76, 77, 78, 79, 80, 81, 85, 86, 88, 90, 93, 96, 98, 99}

set_b = {0, 1, 8, 16, 17, 18, 22, 24, 29, 31,
         33, 34, 36, 42, 46, 47, 51, 53, 62, 64, 65, 66, 67}

res = set_a | set_b
print(len(res))

set_a = {31, 37, 39, 41, 47, 58, 60, 62, 70, 75,
         76, 77, 78, 79, 80, 81, 85, 86, 88, 90, 93, 96, 98, 99}

set_b = {0, 1, 8, 16, 17, 18, 22, 24, 29, 31,
         33, 34, 36, 42, 46, 47, 51, 53, 62, 64, 65, 66, 67}


res_1 = set_a - set_b
res_2 = set_b - set_a
print(len(res_1))
print(len(res_2))



n = int(input())
listok = []
for i in range(n):
    listok.append(list(map(int, input().split())))
for item in listok:
    print(len(set(item)))



n = int(input())
listok = []
new = set()
for i in range(n):
    listok.append(list(map(int, input().split())))
for i in listok:
    new.update(i)

print(len(new))


phrases = list(map(str,input().lower().split(',')))
check_set = set()
for i in phrases:
    if i in check_set:
        print('ДА')
        check_set.add(i)
    else:
        print('НЕТ')
        check_set.add(i)


a = set(map(int,input().split()))
b = set(map(int,input().split()))
new_set = a.intersection(b)
new_set = list(new_set)
new_set.sort()
print(*new_set)


a = set(map(int,input().split()))
b = set(map(int,input().split()))
a = a.difference(b)
a = list(a)
a.sort()
print(*a)




text = input()
new = set()
comp = []
for i in text:
    if i.isdigit() and text.count(i)>1:
        new.add(int(i))
new = list(new)
new.sort()
print ("NO") if len(new) == 0 else print (*new)

text = input()
new = set()
new_text = ''
for i in text:
    if i not in new:
        new.add(i)
        new_text += i

print(new_text)


listok =[int(i * '7') for i in range(1,78)]
my_frozen = frozenset(listok)


words = ['feel', 'graduate', 'movie', 'fashionable', 'bacon',
         'drop', 'produce', 'acquisition', 'cheap', 'strength',
         'master', 'perception', 'noise', 'strange', 'am']

words_with_position =  []
for ind, item in enumerate(words,1):
    words_with_position.append((item,ind))
print(words_with_position)


english_words = ('attack', 'bless', 'look', 'reckless', 'short', 'monster', 'trolley', 'sound',
                 'ambiguity', 'researcher', 'trunk', 'coat', 'quantity', 'question', 'tenant',
                 'miner', 'definite', 'kit', 'spectrum', 'satisfied', 'selection', 'carve',
                 'ask', 'go', 'suggest')


for ind, item in enumerate(english_words,1):
    print(f'Word № {ind} = {item}')


#Алгоритм Луна
num = list(input())
new =[]

for ind, item in enumerate(num,1):
    if ind%2 == 0:
        new.append(int(item))
    else:
        res = int(item)*2
        if res<10:
            new.append(res)
        else:
            new.append(res-9)

res = True if sum(new)%10 == 0 else False
print(res)

def get_body_mass_index (mass,leight):
    index = int(mass/(leight/100)**2)
    if index < 18.5:
        print('Недостаточная масса тела')
    elif 18.5 <= index <= 25:
        print('Норма')
    else:
        print('Избыточная масса тела')
