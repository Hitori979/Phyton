print('Возможные операторы: +, -, *, /')
print('vs - возведение в степень, m - модуль, r - рандом, ! - факториал, ac - арккосинус')
print('Для выхода наберите выход')
Operator = input("Введите оператор : ")

def plus(x1, x2):
    print("Сумма = ", float(x1 + x2))


def minus(x1, x2):
    print("Разность = ", float(x1 - x2))


def multi(x1, x2):
    print("Произведение = ", float(x1 * x2))


def div(x1, x2):
    print("Частное = ", float(x1 / x2))


def exp(x1, x2):
    print(x1, "в степени", x2, "=", float(x1 ** x2))


def mod(x1):
    print("Модуль числа = ", float(abs(x1)))


def rand(x1, x2):
    print("Случайное число = ", random.uniform(x1, x2))


def fact(x1):
    print(x1, "! = ", math.factorial(x1))


def arc(x1):
    print("Арккосинус", x1, "=", math.acos(x1), "рад")


while Operator != "выход":
    if Operator == "+":
        plus(float(input("Первое число: ")), float(input("Второе число: ")))
    elif Operator == "-":
        minus(float(input("Первое число: ")), float(input("Второе число: ")))
    elif Operator == "*":
        multi(float(input("Первое число: ")), float(input("Второе число: ")))
    elif Operator == "/":
        div(float(input("Первое число: ")), float(input("Второе число: ")))
    elif Operator == "^":
        exp(float(input("Первое число: ")), float(input("Второе число: ")))
    elif Operator == "m":
        mod(float(input("Введите число: ")))
    elif Operator == "r":
        rand(float(input("Введите верхнюю границу случайного числа: ")),
         float(input("Введите нижнюю границу случайного числа: ")))
    elif Operator == "!":
        fact(int(input("Введите целое неотрицательное число: ")))
    elif Operator == "ac":
        arc(float(input("Введите число в диапазоне от -1 до 1: ")))
    Operator = input("Введите оператор : ")