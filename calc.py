flag1 = "Д"
while flag1 == "Д":
    flag2 = True
    summa = 0
    print('Если вы хотите закончить ввод чисел, введите "З"')
    while flag2:
        a = input()
        if a.isdigit():
            summa += int(a)
        elif a == "З":
            print(summa)
            flag2 = False
        else:
            print("Ошибка ввода")
    flag1 = input("Хотите продолжить? Д/н: ")