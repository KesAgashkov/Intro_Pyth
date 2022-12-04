# str = input()
# char = str[-1]
# full = char+str
# print(full[:-1])
#
# s = input()
# s = s.lower()
# wor = s[:3].upper()
# w = s[3:-3]
# p = s[-3:].upper()
#
# print(wor+w+p)
# s = input()
# s = s.lower()
# print(s.count('e'))
#
# s = input()
# print(s.replace('w', '').replace('z', ''))
#
# s = input()
# s = s.lower().replace('a', '').replace('o', '').replace('y', '').replace('e', '').replace('u', '').replace('i', '')
# p = '.'
# s = s.replace('', '.')
# print(s[0:-1])
#
# list_strings = ['Follow', 'the', 'Cops', 'Back', 'Home']
# print('-'.join(list_strings))
#
# # преобразование входящих данных в код RGB
# r = hex(int(input())).lstrip('0x').zfill(2).upper()
# g = hex(int(input())).lstrip('0x').zfill(2).upper()
# b = hex(int(input())).lstrip('0x').zfill(2).upper()
# print(f'#{r}{g}{b}')
#
# number_pi = 3.141592653589793
#
#
# print(f'{number_pi:.6f}')
# n = int(input())
# print(f'{n:010d}')

# APPLES = .50
# BREAD = 1.50
# CHEESE = 2.25
# num_apples = 3
# num_bread = 10
# num_cheese = 6
# price_apples = num_apples * APPLES
# price_bread = num_bread * BREAD
# price_cheese = num_cheese * CHEESE
# str_apples = 'Яблоки'
# str_bread = 'Хлеб'
# str_cheese = 'Сыр'
# total = price_bread + price_cheese + price_apples
# print(f'{"Список покупок":^30s}')
# print(f'{"=" * 30}')
# print(f'{str_apples:10s}{num_apples:10d}\t${price_apples:>5.2f}')
# print(f'{str_bread:10s}{num_bread:10d}\t${price_bread:>5.2f}')
# print(f'{str_cheese:10s}{num_cheese:10d}\t${price_cheese:>5.2f}')
# print(f'{"Total:":>20s}\t${total:>5.2f}')

a=[1,100,3]
b = a
a[0]=100
print(b,a)

print(see_walrus := 'Look at my walrus, my walrus is amazing') #пример моржового оператора

string_1 = input()
string_2 = input()
if string_1 == string_2[::-1]:
    print('YES')
else:
    print('NO')

num = int(input())
if num%10 == num//1000 and num%100//10 == num%1000//100:
    print('YES')
else:
    print('NO')




