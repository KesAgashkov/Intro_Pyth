# Работаем с JSON в Python. Парсинг JSON, сохраняем JSON в файл
# JSON - это текстовый формат обменна данными
# преобразуем в пеновский объект при помощи
# функция load когда мы считываем файлик json
# loads когда мы считываем строку в формате json
# метод damp создаёт файлик
# метод damps создаёт строку в виде json
import json
from pprint import pprint

from random import randint
from datetime import datetime
# str_json = """
# {
#     "response": {
#         "count": 5961878,
#         "items": [{
#             "first_name": "Елизавета",
#             "id": 620471795,
#             "last_name": "Сопова",
#             "can_access_closed": true
#         }, {
#             "first_name": "Роман",
#             "id": 614752515,
#             "last_name": "Малышев",
#             "can_access_closed": true
#         }]
#     }
# }"""
# print(type(str_json))
#
# data = json.loads(str_json)
# print(type(data))  # проверяем какой тип объекта
# # так как items список можно его обойти циклом for
# for item in data["response"]["items"]:
#     print(item["first_name"], item["last_name"])
#     # этим мы распарсили эту джейсонину
#
# # создаём собственную джейсонину
# for item in data["response"]["items"]:
#     del item['id']  # удаляем один ключ
#     item['a'] = None  # добавляем None в джесоне это будет null
#     item['likes'] = randint(100, 200)  # добавляем словарь лайков
#     item['now'] = datetime.now().strftime('%d/%m/%y')  # нужно преобразовать в одному из пазовых типов который поддерживает джесон
# print(data["response"]["items"])
# # создаём новую джейсонину из нового словарика
# new_json = json.dumps(data, indent=2)  # функция dumps к которой мы передаём объект который хотим превратить в джесон
# print(new_json)
# # очень часто джесон нужно будет сохранять в виде файла
# with open('my.json', 'w') as file:  # создаём файл
#     json.dump(data, file, indent=3) # indent для красоты вывода
#
# with open("my_json", 'r') as file:  # загружаем наши данные из файлика в переменную data
#     date = json.load(file)
# print(data)


#Провели сериализацию. Перевели словарь питона в формат json
# import json
# data = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
# json_data = json.dumps(data)
# print(json_data)




# with open("manager_sales.json", 'r') as file:  # загружаем наши данные из файлика в переменную data
#     summ = 0
#     date = json.load(file)
#     print(type(date))
#     new = []
#     for item in date:
#         for i in item["cars"]:
#             summ += int(i["price"])
#         else:
#             data = f'{item["manager"]["first_name"]} {item["manager"]["last_name"]} {summ}'
#             new.append(data)
#             summ = 0
#
# with open("group_people.json", 'r') as file:
#     date = json.load(file)
#     new = []
#     count = 0
#     data = ''
#     for i in date:
#         for item in i['people']:
#             if int(item['year']) > 1977 and item['gender'] == 'Female':
#                 count+=1
#         else:
#             data = f"{i['id_group']} {count}"
#             new.append(data)
#             count = 0
#
# pprint(new)


# with open('Abracadabra__1_.txt', encoding='utf-8') as abra, open('Alphabet.json', encoding='utf-8') as alph:
#
#     data = json.load(alph)
#
#     text = abra.read()
#
#     for i in text:
#
#         print(data.setdefault(i, i), end='')



# import json
# people = '[{"name": "Haley Whitney", "country": "British Indian Ocean Territory (Chagos Archipelago)", "age": 54}, {"name": "Matthew King", "country": "Colombia", "age": 34}, {"name": "Sean Sullivan", "country": "Mayotte", "age": 40}, {"name": "Christian Crawford", "country": "Russian Federation", "age": 29}, {"name": "Sarah Contreras", "country": "Honduras", "age": 82}, {"name": "Danielle Williams", "country": "Togo", "age": 91}, {"name": "Jonathan Wilson", "country": "Tunisia", "age": 49}, {"name": "Patricia Wilkerson", "country": "Georgia", "age": 22}, {"name": "Zachary Scott", "country": "Brunei Darussalam", "age": 55}, {"name": "Elizabeth Sanchez", "country": "Nauru", "age": 23}, {"name": "Christina Fernandez", "country": "Burundi", "age": 71}, {"name": "Allen Norton", "country": "Montserrat", "age": 79}, {"name": "Scott Arroyo", "country": "Montenegro", "age": 72}, {"name": "Brooke Boyd", "country": "Latvia", "age": 74}, {"name": "Jerry Morrow", "country": "San Marino", "age": 23}, {"name": "Danielle Bradshaw", "country": "Vietnam", "age": 64}, {"name": "Jerry Thompson", "country": "Belgium", "age": 30}, {"name": "Mark Jordan", "country": "Comoros", "age": 89}, {"name": "Joseph Berger", "country": "Cook Islands", "age": 94}, {"name": "Gina Brooks", "country": "Samoa", "age": 51}, {"name": "Walter Duran", "country": "Chad", "age": 67}, {"name": "John Martinez", "country": "Wallis and Futuna", "age": 65}, {"name": "Johnny Glover", "country": "Eritrea", "age": 72}, {"name": "Lindsay Moore", "country": "Liberia", "age": 53}, {"name": "Kimberly Burton", "country": "Nicaragua", "age": 92}, {"name": "Jacqueline Ballard", "country": "Nigeria", "age": 78}, {"name": "Charles Thompson", "country": "Saudi Arabia", "age": 50}, {"name": "Suzanne Roberts", "country": "Serbia", "age": 43}, {"name": "David Decker", "country": "South Africa", "age": 71}, {"name": "Christopher Perez", "country": "Cayman Islands", "age": 49}, {"name": "Debra Hall", "country": "Greece", "age": 13}, {"name": "John King", "country": "Bahamas", "age": 40}, {"name": "Justin Galvan", "country": "Namibia", "age": 19}, {"name": "Jacqueline Berger", "country": "Yemen", "age": 59}, {"name": "Shawn Robinson", "country": "Saint Pierre and Miquelon", "age": 32}, {"name": "Kristen Garcia", "country": "Portugal", "age": 48}, {"name": "Christopher Barry", "country": "French Polynesia", "age": 23}, {"name": "Alejandra Cook", "country": "Egypt", "age": 16}, {"name": "Jill Harrell", "country": "Comoros", "age": 49}, {"name": "Sara Zimmerman", "country": "Brazil", "age": 26}, {"name": "Mrs. Charlene Flores", "country": "New Caledonia", "age": 75}, {"name": "Melissa Crawford", "country": "Lebanon", "age": 17}, {"name": "Larry Wong", "country": "New Caledonia", "age": 6}, {"name": "Brenda Acosta", "country": "Grenada", "age": 48}, {"name": "Latoya Terry", "country": "Saint Martin", "age": 41}, {"name": "Seth Luna", "country": "Sao Tome and Principe", "age": 59}, {"name": "Micheal Adams", "country": "Barbados", "age": 53}, {"name": "Susan Carroll", "country": "Somalia", "age": 64}, {"name": "Douglas Morris", "country": "Thailand", "age": 24}, {"name": "Dennis Wagner", "country": "Zimbabwe", "age": 66}, {"name": "Kristin Johnson", "country": "Niue", "age": 71}, {"name": "Steven Krause", "country": "Turkmenistan", "age": 84}, {"name": "Jared Smith", "country": "Colombia", "age": 46}, {"name": "Lauren Anderson", "country": "Christmas Island", "age": 46}, {"name": "Joshua Spencer", "country": "Russian Federation", "age": 38}, {"name": "Maria Edwards", "country": "Hungary", "age": 78}, {"name": "Anne Lee", "country": "United States of America", "age": 10}, {"name": "James Mckenzie", "country": "Uganda", "age": 43}, {"name": "Joshua Gallegos", "country": "United States Minor Outlying Islands", "age": 27}, {"name": "Paul Herrera", "country": "Kiribati", "age": 17}, {"name": "Veronica White", "country": "Gabon", "age": 88}, {"name": "Michael Hall", "country": "China", "age": 43}, {"name": "Sabrina Thompson", "country": "Chad", "age": 27}, {"name": "Jennifer Archer", "country": "Korea", "age": 45}, {"name": "Christina Simmons", "country": "Israel", "age": 80}, {"name": "Travis White", "country": "Central African Republic", "age": 31}, {"name": "Dennis Hernandez", "country": "Slovenia", "age": 66}, {"name": "Matthew Richards", "country": "Svalbard & Jan Mayen Islands", "age": 34}, {"name": "Stephen Curry", "country": "Finland", "age": 92}, {"name": "Margaret Williamson", "country": "Hong Kong", "age": 86}, {"name": "Mary Estes", "country": "Montenegro", "age": 19}, {"name": "Alex Scott", "country": "Christmas Island", "age": 67}, {"name": "John Andrews", "country": "Bahamas", "age": 68}, {"name": "Jonathan Willis", "country": "Saint Martin", "age": 23}, {"name": "Olivia Campos", "country": "Armenia", "age": 72}, {"name": "Diana Davis", "country": "Azerbaijan", "age": 54}, {"name": "Jack Cummings", "country": "Martinique", "age": 94}, {"name": "Kaitlyn Mcdonald", "country": "Austria", "age": 12}, {"name": "Maria Blake", "country": "Pitcairn Islands", "age": 91}, {"name": "Kelly Thomas", "country": "Ethiopia", "age": 74}, {"name": "John Terrell Jr.", "country": "India", "age": 50}, {"name": "Lindsay Wood", "country": "United Arab Emirates", "age": 72}, {"name": "Matthew Gilbert", "country": "Madagascar", "age": 86}, {"name": "Tanner Johnson", "country": "Congo", "age": 11}, {"name": "Michael Garcia", "country": "Liberia", "age": 45}, {"name": "Nicole Johnson", "country": "Barbados", "age": 54}, {"name": "William Lee", "country": "Lithuania", "age": 59}, {"name": "Jeffrey Coffey", "country": "Faroe Islands", "age": 88}, {"name": "Sandra Freeman", "country": "Philippines", "age": 35}, {"name": "Latoya Maxwell", "country": "Sweden", "age": 12}, {"name": "Darius Blevins", "country": "Thailand", "age": 29}, {"name": "Teresa Newman", "country": "Jersey", "age": 6}, {"name": "Larry Bray", "country": "Brunei Darussalam", "age": 21}, {"name": "Adam Roberson", "country": "Jordan", "age": 71}, {"name": "Michael Gomez", "country": "Tajikistan", "age": 37}, {"name": "Abigail Mccarthy", "country": "Kiribati", "age": 85}, {"name": "Tom Morris", "country": "Cayman Islands", "age": 27}, {"name": "Kevin Wagner", "country": "Suriname", "age": 55}, {"name": "Peggy Bryant", "country": "Korea", "age": 36}, {"name": "Erik Mclaughlin", "country": "Austria", "age": 24}]'
# data = json.loads(people)
# data = sorted(data,  key=lambda x: (x['age'], x['name']))
#
# for i in data:
#     print(f"{i['name']}, {i['country']}, {i['age']}")




# json_string = '''
# {
#     "customers": [
#         {
#             "userid": 123456,
#             "username": "Allie Hsu",
#             "phone": [
#                 "000-001-0002",
#                 "000-002-0002"
#             ],
#             "is_vip": true
#         },
#         {
#             "userid": 223678,
#             "username": "Donald Duck",
#             "phone": null,
#             "is_vip": false
#         }
#     ]
# }
# '''
#
# data = json.loads(json_string)
# print(data['customers'][0]['username'])



# words = ['feel', 'graduate', 'movie', 'fashionable', 'bacon', 'drop', 'produce', 'acquisition',
#          'cheap', 'strength', 'master', 'perception', 'noise', 'strange', 'am']
#
# lens = iter(words)
# for i in lens:
#     print(len(i))


days =(j for j in range(1,78))
spis = ['Saturday','Sunday','Monday','Tuesday','Wednesday','Thursday', 'Friday']
for i in range(77):
    print((next(days),spis[i%7]))