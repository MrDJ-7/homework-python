# 1
n = 23
for i in range(1, n+5):
    print(i)
# 2
m = int(input('m='))
k = int(input('k='))
for i in range(m, k):
    print(i)
# 3
s = 0
while True:
    x = int(input(''))
    if x == 0:
        break
    s += x
print(s)
# 4
a = input()
print(a[::2])
# 5
b = input()
k = 0
for i in b:
    if (i == '*'):
        k += 1
print(k)
# 6
c = input()
print(c[::-1])
# 7
d = input()
print(d[6::7])
