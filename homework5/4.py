def num_check(user_num):
    num = user_num
    try:
        num = int(num)
    except:
        num = num_check(input("Вы вместо числа ввели строку. Введите число: "))
    return num

def sequence(n, res = (-2)):
    if n == 0 and res == (-2):
        print("последовательность не имеет чисел")
        #return None
    else:
        if n == 0:
            print(res)
            return res
        res *= (-.5)
        sequence(n-1, res)
    

sequence(num_check(input("Введите число: ")))