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