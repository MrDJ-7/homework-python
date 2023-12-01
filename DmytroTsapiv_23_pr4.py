def draw_triangle():
    for i in range(10):
        print('*' * (i + 1))


def draw_rectangle():
    for i in range(14):
        if i == 0 or i == 13:
            print('*' * 10)
        else:
            print('*' + ' ' * 8 + '*')


def draw_triangle1(fill, base):
    for i in range(base):
        if i < (base // 2):
            print(fill * (i + 1))
        else:
            print(fill * (base - i))


def print_digit_sum(num):
    digit_sum = 0
    for i in str(num):
        digit_sum += int(i)
    print(digit_sum)


def merge_list(lst1, lst2):
    lst1.extend(lst2)
    for i in range(len(lst1)):
        for j in range(i):
            if(lst1[i]<lst1[j]):
                lst1[i], lst1[j] = lst1[j], lst1[i]
        
    return lst1


def get_middle_point(x1, y1, x2, y2):
    return (x1 + x2) / 2, (y1 + y2) / 2


def solve(a, b, c):
    x1 = (-b - (b**2 - 4 * a * c)**(1 / 2)) / (2 * a)
    x2 = (-b + (b**2 - 4 * a * c)**(1 / 2)) / (2 * a)
    if (x1 > x2):
        x1, x2 = x2, x1
    return x1, x2


# print("завдання №")

draw_triangle()

draw_rectangle()

fill = input("fill = ")
base = int(input("base = "))
draw_triangle1(fill, base)

print_digit_sum(int(input("num = ")))

lst1 = list(map(int, input("lst1 = ").split()))
lst2 = list(map(int, input("lst2 = ").split()))
print(merge_list(lst1, lst2))

x1 = int(input("x1 = "))
y1 = int(input("y1 = "))
x2 = int(input("x2 = "))
y2 = int(input("y2 = "))
print(get_middle_point(x1, y1, x2, y2))

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
print(solve(a, b, c))
