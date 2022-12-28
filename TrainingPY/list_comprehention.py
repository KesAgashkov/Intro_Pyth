n = int(input())
el  = [i for i in range(1,n+1) if n%i == 0]
print(el)

n = int(input())
el  = [i for i in range(n,n**2+1) if i%2 != 0]
print(el)


a,b = map(int,input().split())
res = [i**2 for i in range(a,b+1)] if a<b else [i**3 for i in range(a,b-1,-1)]
print(res)

st = "Create a list of the first letters of every word in this string"
st = [i[0] for i in st.split()]
print(st)

from string import ascii_uppercase
n = int(input())
s = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
print(s[0:n])

from string import ascii_uppercase
n = int(input())
s = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
s = [s[i]*(i+1) for i in range(n)]
print(s)

phrase = 'Take only the words that start with t in this sentence'
list = [i for i in phrase.split() if i[0] == "T" or i[0] == "t"]
print(list)

i_love_none = [None for i in range(50)]
print(i_love_none)


