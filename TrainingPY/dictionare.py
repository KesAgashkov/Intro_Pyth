# # person = dict(name='Vasya', surname='Petrov', age=25)
# # print(person)
# #
# # sweet = {
# #     "id": "0001",
# #     "type": "donut",
# #     "name": "Cake",
# #     "ppu": 0.55,
# #     "calories": 125,
# # }
# # print(sweet["name"])
# # print(sweet["calories"])
# # print(sweet["id"])
# #
# # num = int(input())
# # days = {
# #     1: 31,
# #     2: 28,
# #     3: 31,
# #     4: 30,
# #     5: 31,
# #     6: 30,
# #     7: 31,
# #     8: 31,
# #     9: 30,
# #     10: 31,
# #     11: 30,
# #     12: 31
# # }
# # print(days[num])
# #
# #
# #
# #
# # n = int(input())
# # dic = dict([[i,i**2] for i in range(1,n+1)])
# # print(dic)
# #
# # from string import ascii_lowercase
# #
# # text = ascii_lowercase
# # alphabet = dict([[text[i-1],i] for i in range(1,27)])
# # print(alphabet)
#
# cur = input()
# currencies = {
#     'Argentine Peso': 118362.205708,
#     'Australian Dollar': 1586.232315,
#     'Bahraini Dinar': 423.780164,
#     'Botswana Pula': 13168.450636,
#     'Brazilian Real': 5954.781483,
#     'British Pound': 834.954104,
#     'Bruneian Dollar': 1520.451015,
#     'Bulgarian Lev': 1955.83,
#     'Canadian Dollar': 1430.54405,
#     'Chilean Peso': 898463.818465,
#     'Chinese Yuan Renminbi': 7171.445692,
#     'Colombian Peso': 4447741.922165,
#     'Croatian Kuna': 7527.744707,
#     'Czech Koruna': 24313.797041,
#     'Danish Krone': 7440.613895,
#     'Emirati Dirham': 4139.182587,
#     'Hong Kong Dollar': 8786.255952,
#     'Hungarian Forint': 355958.035747,
#     'Icelandic Krona': 143603.932438,
#     'Indian Rupee': 84241.767127,
#     'Indonesian Rupiah': 16187150.010697,
#     'Iranian Rial': 47534006.535121,
#     'Israeli Shekel': 3569.191411,
#     'Japanese Yen': 129149.364679,
#     'Kazakhstani Tenge': 489292.515538,
#     'Kuwaiti Dinar': 340.959682,
#     'Libyan Dinar': 5196.539901,
#     'Malaysian Ringgit': 4717.485104,
#     'Mauritian Rupee': 49212.933037,
#     'Mexican Peso': 23130.471272,
#     'Nepalese Rupee': 134850.008728,
#     'New Zealand Dollar': 1703.649473,
#     'Norwegian Krone': 9953.078431,
#     'Omani Rial': 433.360301,
#     'Pakistani Rupee': 198900.635421,
#     'Philippine Peso': 57574.278782,
#     'Polish Zloty': 4579.273862,
#     'Qatari Riyal': 4102.552652,
#     'Romanian New Leu': 4946.638369,
#     'Russian Ruble': 86197.012666,
#     'Saudi Arabian Riyal': 4226.530892,
#     'Singapore Dollar': 1520.451015,
#     'South African Rand': 17159.831129,
#     'South Korean Won': 1355490.097163,
#     'Sri Lankan Rupee': 228245.645722,
#     'Swedish Krona': 10439.125427,
#     'Swiss Franc': 1037.792217,
#     'Taiwan New Dollar': 31334.286611,
#     'Thai Baht': 37436.518169,
#     'Trinidadian Dollar': 7636.35428,
#     'Turkish Lira': 15078.75981,
#     'US Dollar': 1127.074905,
#     'Venezuelan Bolivar': 511082584.868731
# }
# if cur in currencies:
#     print(currencies[cur])
# else:
#     print(f"Нет данных по {cur}")
#
#
# account = {
#   "id": 3136,
#   "uid": "1359acc6-f07a-4a2a-984e-3fb809982948",
#   "account_number": "0847799459",
#   "iban": "GB90XTND56373623909314",
#   "bank_name": "ABN AMRO HOARE GOVETT CORPORATE FINANCE LTD.",
#   "routing_number": "126602476",
#   "swift_bic": "BCYPGB2LHGB"
# }
# keys = list(account)
# print(keys)
#
#
# d1 = {'India': 'Delhi',
#       'Canada': 'Ottawa',
#       'United States': 'Washington D. C.'}
#
# d2 = {'France': 'Paris',
#       'Malaysia': 'Kuala Lumpur'}
# capitals =  d1|d2
# print(capitals)

# d={}
# n=int(input())
# for i in range(n):
#     x=input()
#     if x in d:
#         print(f'{x}{d[x]}')
#         d[x]+=1
#
#     else:
#         print('OK')
#         d[x]=1
#
# countries = {
#     "Sweden": ["Stockholm", "Göteborg", "Malmö"],
#     "Norway": ["Oslo", "Bergen", "Trondheim"],
#     "England": ["London", "Birmingham", "Manchester"],
#     "Germany": ["Berlin", "Hamburg", "Munich"],
#     "France": ["Paris", "Marseille", "Toulouse"]
# }

# city = input()
# for item in countries.items():
#     if city in item[1]:
#         print(f'INFO: {city} is a city in {item[0]}')
#         break
# else:
#     print(f'ERROR: Country for {city} not found')

# user ={'password':3232, 'last_name':'kes'}
# print(user)
# user['surname'] = user.pop('last_name')
# user['secret'] = user.pop('password')
# print(user)
#
s = input()
d = {}
for i in s:
    i = i.lower()
    if i.isalpha():
        d[i] = d.get(i, 0) + 1
print(d)



# workers = {
#     'employer1': {'name': 'Jhon', 'salary': 7500},
#     'employer2': {'name': 'Emma', 'salary': 8000},
#     'employer3': {'name': 'Brad', 'salary': 500}
# }
# workers['employer3']['salary']= 8500
# print(workers)

supermarket = {
    "milk": {"quantity": 20, "price": 1.19},
    "biscuits": {"quantity": 32, "price": 1.45},
    "butter": {"quantity": 20, "price": 2.29},
    "cheese": {"quantity": 15, "price": 1.90},
    "bread": {"quantity": 15, "price": 2.59},
    "cookies": {"quantity": 20, "price": 4.99},
    "yogurt": {"quantity": 18, "price": 3.65},
    "apples": {"quantity": 35, "price": 3.15},
    "oranges": {"quantity": 40, "price": 0.99},
    "bananas": {"quantity": 23, "price": 1.29}
}
sum = 0
for item in supermarket:
    sum += supermarket[item]["quantity"] * supermarket[item]["price"]

print(sum)

s_1 = input()
s_2 = input()
d_1 = {}
d_2 = {}
for i in s_1:
    i = i.lower()
    if i.isalpha():
        d_1[i] = d_1.get(i, 0) + 1
for i in s_2:
    i = i.lower()
    if i.isalpha():
        d_2[i] = d_2.get(i, 0) + 1
if d_1 == d_2:
    print('YES')
else:
    print('NO')
