def num_check(user_num):
    num = user_num
    try:
        num = int(num)
    except:
        num = num_check(input("Вы вместо числа ввели строку. Введите число: "))
    return num

def reverse(val, res = ""):
    if val <= 0:
        print(res)
        return res
    res += str(val % 10)
    reverse(val // 10, res)
reverse(num_check(input("Введите число: ")))