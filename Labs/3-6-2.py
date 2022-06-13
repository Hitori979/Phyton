word1 = input("Введите первый список через запятую: ")


def comma(word1):
    return word1.split(",")


def set1(word1):
    return set(word1)


def lenght(word1):
    return len(word1)


def comma2(w2):
    return w2.split(",")


def set2(w2):
    return set(w2)


print("В списке {} слов(а)".format(len(comma(word1))))
w2 = input("Введите второй список из {} слов через запятую: ".format(len(comma(word1))))

dList = dict(zip(word1.split(","), w2.split(",")))
print(dList)