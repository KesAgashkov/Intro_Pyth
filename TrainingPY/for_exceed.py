# last =0
# summ =0
# fin = 0
# for i in range (1000, 10000):
#     summ = 0
#     p = i
#     for j in range(4):
#         last = i%10
#         summ +=last
#         i //= 10
#         last = 0
#     if summ == 20:
#         fin += p
#         summ=0
# print(fin)
#
# n = int(input())
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j, end=" ")
#     print()
#
# nums = list(map(int,input().split()))
# for i in range(len(nums)):
#     for j in range(nums[i]):
#         print('*', end="")
#     print()


# Постулат Бертрана
n = int(input())
count = 0
type = []
flag = True
for i in range((n + 1), (n * 2)):

    for j in range(2, int(i ** 0.5 + 1)):
        if i % j == 0:
            break
    else:
        count += 1

print(count)

#Старый добрый пузырёк
n = int(input())
nums = list(map(int, input().split()))
min = nums[0]
count = 0
for ran in range(n - 1):
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            x = nums[i + 1]
            nums[i + 1] = nums[i]
            nums[i] = x
            count += 1

print(*nums)
print(count)

# Решение системы уравнений методом перебора а и б

n, m = map(int, input().split())
count = 0
for a in range(33):
    for b in range(33):
        if (a ** 2 + b == n) and (a + b ** 2 == m):
            count += 1

print(count)