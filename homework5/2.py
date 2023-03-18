def num_check(user_num):
    num = user_num
    try:
        num = int(num)
    except:
        num = num_check(input("Вы вместо числа ввели строку. Введите число: "))
    return num

def counter(val, even = 0, odd = 0):
    if val <= 0:
        print(f"четных: {even}, нечетных: {odd}")
        return None
    if val % 10 % 2 == 0:
        even+=1
    else:
        odd+=1
    counter(val // 10, even, odd)
counter(num_check(input("Введите число: ")))
