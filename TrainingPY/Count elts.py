# #Подсчёт количества цифр
# s=list(map(int,str(input())))
# count=[0]*10
# for i in s:
#     count[i] += 1
# for i in range(10):
#     if count[i]>0:
#         print(i,count[i])

n = int (input())
s=list(map(int,input().split()))
minn = s[0]
new = []
i = 0
for i in range(n):
    new.append(min(s))
    s.remove(min(s))
print(*new)
