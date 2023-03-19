def num_check(user_num):
    num = user_num
    try:
        num = float(num)
    except:
        num = num_check(input("Вы вместо числа ввели строку. Введите число: "))
    return num
def calc():
    x = input("Введите операцию (+, -, *, / или 0 для выхода): ")
    if x == 0:
        return("Программа завершена")
    if x != "+" and x != "-" and x != "*" and x != "/":
        print("Вы ввели иное значение.")
        calc()
    else:
        a = num_check(input("Введите первое число: "))
        b = num_check(input("Введите второе число: "))
        if x == "+":
            res = a + b
        elif x == "-":
            res = a - b
        elif x == "*":
            res = a * b
        elif x == "/":
            if b == 0:
                res = "Делить на ноль нельзя!"
            else:
                res = a / b
        print(f"{a} {x} {b} = {res}")
        calc()
calc()