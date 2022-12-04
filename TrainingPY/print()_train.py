# a, b, c, d = map(int, input().split())
# print(float((a+b+c+d)/4))
#
# a, b, c, d, e = map(int, input().split())
# print(max(a,b,c,d,e))
#
# s = int(input())
# p = c = int(1/6*s)
# k = int(p*4)
# print(p,k,c)
#
# g, l = map(int, input().split())
# whole = g+l-1
# print((whole-g), (whole-l))
# print(input(),end = '---')
# print(input(),end = '---')
# print(input())

# s = input()
# num = int(input().split())
# print(num)
#
# num=int(input())
# hours = num//60
# minuts = num % 60
# after = hours // 24
# hours = hours - (after*24)
# print(hours,minuts)

#

# a, b = map(int, input().split())
# c = (a % 7 == 0) and (a % 7 == 0)
# print(c)

a, b, c = map(str, input().split())
a_ord = ord(a)
b_ord = ord(b)
c_ord = ord(c)
print(f'''Simvol code {a} is {a_ord}.
Simvol code {b} is {b_ord}.
Simvol code {c} is {c_ord}.''')

num = int(input())
num = str(num)
num = num.zfill(6)
if (int(num[0]) + int(num[1]) + int(num[2])) == (int(num[-1]) + int(num[-2]) + int(num[-3])):
    print('YES')
else:
    print('NO')

