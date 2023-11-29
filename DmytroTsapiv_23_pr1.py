# Задвання 1
print("Мене звати Цапів Дмитро, я в списку 23")

# Задвання 2
print("Я", "люблю", "Python", sep="-", end="<3\n")

# Задвання 3
a = int(input("A = "))
b = int(input("B = "))
c = int(input("C = "))
print("sum = ", a+b+c)

# Задвання 4
d = float(input("D = "))
print("V = ", d ** 3, "\nS = ", 6*(d**2))

# Задвання 5
time = int(input("Time = "))
print(time//60, 'год ', time % 60, 'хв')

# Задвання 6
e = int(input('E = '))
print('парне' if e % 2 == 0 else 'непарне')

# Задвання 7
s = 0
a = int(input("A = "))
b = int(input("B = "))
c = int(input("C = "))
s += a if a > 0 else 0
s += b if b > 0 else 0
s += c if c > 0 else 0
print(s)

# Задвання 8
f = int(input("F = "))
if f//1000 > 1 and f//1000 < 10 and (f % 7 == 0 or f % 17 == 0):
    print('beautiful')
else:
    print('Not beautiful')

# Задвання 9
a = int(input("A = "))
b = int(input("B = "))
c = int(input("C = "))

if a + b > c and c+b > a and a+c > b:
    print(True)
else:
    print(False)
