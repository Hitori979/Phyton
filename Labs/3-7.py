class Calculator:

    def plus(self, x1, x2):
        print("Сумма = ", float(x1 + x2))


    def minus(self, x1, x2):
        print("Разность = ", float(x1 - x2))


    def multi(self, x1, x2):
        print("Произведение = ", float(x1 * x2))


    def div(self, x1, x2):
        print("Деление = ", float(x1 / x2))


    def exp(self, x1, x2):
        print(x1, "в степени", x1, "=", float(x1 ** x2))


    def mod(self, x1):
        print("Модуль числа = ", float(abs(x1)))


    def rand(self, x1, x2):
        print("Случайное число = ", random.uniform(x1, x2))


    def fact(self, x1):
        print(x1, "! = ", math.factorial(x1))


    def arc(self, x1):
        print("Арккосинус", x1, "=", math.acos(x1), "рад")


c = Calculator()

print('Возможные операторы: +, -, *, /')
print('vs - возведение в степень, m - модуль, r - рандом, ! - факториал, ac - арккосинус')
print('Для выхода наберите exit')
Operator = input("Введите оператор : ")
while Operator != "exit":
    if Operator == "+":
        c.plus(float(input("Первое число: ")), float(input("Второе число: ")))
    elif Operator == "-":
        c.minus(float(input("Первое число: ")), float(input("Второе число: ")))
    elif Operator == "*":
        c.multi(float(input("Первое число: ")), float(input("Второе число: ")))
    elif Operator == "/":
        c.div(float(input("Первое число: ")), float(input("Второе число: ")))
    elif Operator == "vs":
        c.exp(float(input("Первое число: ")), float(input("Второе число: ")))
    elif Operator == "m":
        c.mod(float(input("Введите число: ")))
    elif Operator == "r":
        c.rand(float(input("Введите верхнюю границу случайного числа: ")),
               float(input("Введите нижнюю границу случайного числа: ")))
    elif Operator == "!":
        c.fact(int(input("Введите целое неотрицательное число: ")))
    elif Operator == "ac":
        c.arc(float(input("Введите число в диапазоне от -1 до 1: ")))
    Operator = input("Введите оператор : ")
