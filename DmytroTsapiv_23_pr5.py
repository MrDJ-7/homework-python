import math
import random
import time

# 1
a = int(input('a = '))
print(math.sin(a), math.cos(a), math.tan(a), sep="\n")

# 2
print("[a:b]")
l = []
k = int(input('k = '))
a = int(input('a = '))
b = int(input('b = '))
for i in range(k):
    l.append(random.randint(a, b))
print(*l)

# 3
b = random.randint(1, 100)
i = 1
a = int(input('try 1:'))
while a != b:
    if (a > b):
        print("Забагато")
        i += 1
        a = int(input(f'спроба {i}:'))
    else:
        print("Замало")
        i += 1
        a = int(input(f'спроба {i}:'))

print(f'Вітаю, ви вгадали за {i} спроб')

# 4
print('Привіт, я магічна куля i я знаю відповідь на будь яке запитання.')

while True:
    time.sleep(random.randint(2, 5))
    print("Про що ви хочете спитати?")
    a = input()
    list = [
        "Так, це можливо.",
        "Ні, цього не станеться.",
        "Можливо, але важко сказати точно.",
        "Спробуйте ще раз пізніше.",
        "Здається, ви знаєте відповідь самі.",
        "Впевнено так!",
        "Не розраховуйте на це.",
        "Це схоже на гарну ідею!"
    ]
    l = random.choice(list)
    time.sleep(random.randint(2, 5))
    print(l)
    time.sleep(random.randint(2, 5))
    print('Бажаєте ще про щось спитати?')
    a = input()
    if a == 'ні' or a == 'Ні':
        break

print("Повертайтесь як виникнуть питання")
