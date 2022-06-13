print('Возможные операторы: +, -, *, /')
print('vs - возведение в степень, m - модуль, r - рандом, ! - факториал, ac - арккосинус')
operator1 = input("Введите оператор : ")
if operator1 == 'r':
    result = random.uniform(-1000,1000)
else:
    x1 = float(input("Введите первое число : "))
    if operator1 == 'm':
        result = abs(x1)
    elif operator1 == '!':
        x3 = int(abs(x1))
        print("Факториал определен на множестве целых неотрицательных чисел.")
        print("Поэтому посчитаем факториал от ", x3)
        result = math.factorial(x3)
    elif operator1 == 'ac':
        if x1 < -1 or x1 > 1:
            print("Аргумент должен быть в диапазоне от -1 до 1")
        else: result = math.acos(x1)
    else:
        x2 = float(input("Введите второе число : "))
        if operator1 == '+':
            result = x1 + x2
        elif operator1 == '-':
            result = x1 - x2
        elif operator1 == '*':
            result = x1 * x2
        elif operator1 == '/':
            if x2 == 0:
                print("На 0 делить нельзя!")
            else: result = x1 / x2
        elif operator1 == 'vs':
            result = x1 ** x2
print("Результат вычислений : ", result)