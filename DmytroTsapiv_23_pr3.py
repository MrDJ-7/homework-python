# 1
n = int(input('n = '))
a = list(range(1, n+1))
print(a)
# 2
n = int(input('n = '))
# v1
b = list('abcdefghijklmnopqrstuvwxyz')
print(b[0:n])
# v2
# b=[]
# for i in range(n):
#     b.append(chr(ord('a')+i))
# print(b)
# 3
n = int(input('n = '))
c = []
for i in range(n):
    temp = int(input())
    c.append(temp**3)
print(c)
# 4
n = int(input('n = '))
d = []
for i in range(n):
    temp = input()
    d.append(temp)
k = int(input('k = '))
s = ''
for i in d:
    s += ''.join(i[k-1])
print(s)
# 5
n = int(input('n = '))
d = []
for i in range(n):
    temp = input()
    d.append(temp)
k = input('k = ')
s = ''
a = []
for i in d:
    if k in i:
        a.append(i)
print(*a)
# 6
ip = input('ip = ')
num = ip.split('.')
if len(num) != 4:
    print(False)
else:
    for i in num:
        if int(i) < 0 or int(i) > 255:
            print('False')
            break
    else:
        print(True)
# 7
a = input('a = ')
s1 = 0
for i in a:
    s1 += int(i)
print(*a, sep='+', end='='+str(s1))
