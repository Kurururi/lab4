# ************************

def ex1():
    x = int(input("Введите число\n"))

    if x % 3 == 0:
        print("Число делится на 3")
    else:
        print("Число не делится на 3")

# ************************


def ex2(n):
    try:
        n = int(n)
        try:
            d = 100 / n
        except ZeroDivisionError:
            print("На ноль делить нельзя")
        else:
            return d
    except ValueError:
        print("Это не число")

# ************************


def ex3():
    day = int(input("Введите день\n"))
    month = int(input("Введите месяц\n"))
    year = input("Введите год\n")

    y = int(year[2:4])

    return y == day * month
# ************************


def ex4():
    i = 0
    sum1 = 0
    sum2 = 0
    ticket_num = input("Введите номер билета\n")

    if len(ticket_num) % 2 == 0:
        z = len(ticket_num) / 2

        while i < z:
            sum1 += int(ticket_num[i])
            i += 1

        while i < len(ticket_num):
            sum2 += int(ticket_num[i])
            i += 1

        if sum1 == sum2:
            print("Это счастливый билет!")
        else:
            print("Это не счастливый билет...")
    else:
        print("Неподходящий номер билета")

# ************************


ex1()
print(ex2(input()))
print(ex3())
ex4()
