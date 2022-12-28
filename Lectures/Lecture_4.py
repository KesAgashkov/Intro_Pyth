#Азбука Морзе
text = input().lower().split()
mor_text = ''
morze = {'a': '•—', 'b': '—•••', 'c': '—•—•', 'd': '—••',
         'e': '•', 'f': '••—•', 'g': '——•', 'h': '••••',
         'i': '••', 'j': '•———', 'k': '—•—', 'l': '•—••',
         'm': '——', 'n': '—•', 'o': '———', 'p': '•——•',
         'q': '——•—', 'r': '•—•', 's': '•••', 't': '—',
         'u': '••—', 'v': '•••—', 'w': '•——', 'x': '—••—',
         'y': '—•——', 'z': '——••'}
for i in range(len(text)):
    for j in range(len(text[i])):
        for letter, value in morze.items():
            if text[i][j] == letter:
                mor_text+=value+' '
    print(mor_text)
    mor_text = ''

#Преобразование в листа в словарь словарей
persons= [
    ('Allison Hill', 334053, 'M', '1635644202'),
    ('Megan Mcclain', 191161, 'F', '2101101595'),
    ('Brandon Hall', 731262, 'M', '6054749119'),
    ('Michelle Miles', 539898, 'M', '1355368461'),
    ('Donald Booth', 895667, 'M', '7736670978'),
    ('Gina Moore', 900581, 'F', '7018476624'),
    ('James Howard', 460663, 'F', '5461900982'),
    ('Monica Herrera', 496922, 'M', '2955495768'),
    ('Sandra Montgomery', 479201, 'M', '5111859731'),
    ('Amber Perez', 403445, 'M', '0602870126')
]
data ={}
for i in persons:
    data.update({i[0]: {'salary': i[1], 'gender': i[2],  'passport': i[3]}})

data = {'my_friends': {'count': 10, 'items': [
    {'first_name': 'Kurt', 'id': 621547005, 'last_name': 'Cobain', 'bdate': '31.8.2005'},
    {'first_name': 'Виолетта', 'id': 484200150, 'last_name': 'Кастилио'},
    {'first_name': 'Иринка', 'id': 21886133, 'last_name': 'Бушуева', 'bdate': '28.8.1942'},
    {'first_name': 'Данил', 'id': 282456573, 'last_name': 'Греков', 'bdate': '4.7.2002'},
    {'first_name': 'Валентин', 'id': 184902932, 'last_name': 'Долматов', 'bdate': '25.5'},
    {'first_name': 'Евгений', 'id': 620469646, 'last_name': 'Шапорин', 'bdate': '6.12.1982'},
    {'first_name': 'Ангелина', 'id': 622328862, 'last_name': 'Краснова', 'bdate': '4.11.1995'},
    {'first_name': 'Иван', 'id': 576015198, 'last_name': 'Вирин', 'bdate': '2.2.1915'},
    {'first_name': 'Паша', 'id': 386922406, 'last_name': 'Воронов', 'bdate': '27.9'},
    {'first_name': 'Ольга', 'id': 622170942, 'last_name': 'Савченкова', 'bdate': '20.12'}]}}

new = []
for i in data['my_friends']['items']:
    new.append(i['first_name'])

new.sort()
for item in new:
    print(item)

#
# генератор словаря

a = {i: i**2 for i in range(1, 11)}
print(a)

user = {
    "id": 4170,
    "uid": "5e941db5-9e0f-4f94-9fc5-734110c6be14",
    "password": "SyUpfo1ljm",
    "first_name": "Teresa",
    "last_name": "Wehner",
    "username": "teresa.wehner",
    "email": "teresa.wehner@email.com",
    "gender": "Non-binary",
    "phone_number": "+674 424.561.2776",
    "social_insurance_number": "637316241",
    "date_of_birth": "1993-08-17",
    "employment": {
        "title": "Central Hospitality Liaison",
        "key_skill": "Organisation"
    },
    "subscription": {
        "plan": "Essential",
        "status": "Idle",
        "payment_method": "Debit card",
        "term": "Annual"
    }
}
find = list(map(str,input().split()))
data={find[i]:user[find[i]] for i in range(len(find))}
print(data)

people = [
    ['Amy Smith', '694.322.8133x22426'],
    ['Brian Shaw', '593.662.5217x338'],
    ['Christian Sharp', '118.197.8810'],
    ['Sean Schmidt', '9722527521'],
    ['Thomas Long', '163.814.9938'],
    ['Joshua Willis', '+1-978-530-6971x601'],
    ['Ann Hoffman', '434.104.4302'],
    ['John Leonard', '(956)182-8435'],
    ['Daniel Ross', '870-365-8303x416'],
    ['Jacqueline Moon', '+1-757-865-4488x652'],
    ['Gregory Baker', '705-576-1122'],
    ['Michael Spencer', '(922)816-0599x7007'],
    ['Austin Vazquez', '399-813-8599'],
    ['Chad Delgado', '979.908.8506x886'],
    ['Jonathan Gilbert', '9577853541']
]
phone_book= {people[i][1]:people[i][0] for i in range (len(people))}



a = {
    'Sidorov': {'age': 1995, 'hobby': 'soccer', 'car': 'BMW'},
    'Lukov': {'age': 2002, 'hobby': 'basketball', 'car': 'Opel'},
    'Petrov': {'age': 1991, 'hobby': 'chess', 'car': 'BMW'},
    'Gorbachev': {'age': 1984, 'hobby': 'tennis', 'car': 'BMW'},
    'Kostin': {'age': 2000, 'hobby': 'swimming', 'car': 'Audi'},
    'Isaev': {'age': 2005, 'hobby': 'music', 'car': 'BMW'},
    'Eliseev': {'age': 1999, 'hobby': 'chess', 'car': 'Audi'},
    'Kozlov': {'age': 2004, 'hobby': 'soccer', 'car': 'Opel'},
    'Bukov': {'age': 1995, 'hobby': 'basketball', 'car': 'Audi'},
}
cars = [a[elem]['car'] for elem in a]
print(cars)
print('-'*30)
hobbies = [a[elem]['hobby'] for elem in a]
print(hobbies)
print('-'*30)
cars_lt_2000 = [a[elem]['car'] for elem in a if a[elem]['age'] < 2000]
print(cars_lt_2000)
print('-'*30)
name_with_car = [(elem, a[elem]['car']) for elem in a
                        if a[elem]['age'] < 2000]
print(name_with_car)
print('-'*30)
less_2000_and_soccer = [(elem, a[elem]['car']) for elem in a
         if a[elem]['age'] < 2000 and a[elem]['hobby'] == 'soccer']
print(less_2000_and_soccer)


s = 'gfdogjdf45i398gry74y543hgkgreiuYIUGd'
str_digits = [i for i in s if i.isdigit()]
print(str_digits)
print('-'*30)

int_digits = [int(i) for i in str_digits if i.isdigit()]
print(int_digits)

print('-'*30)
letters = [i for i in s if i.isalpha()]
print(letters)