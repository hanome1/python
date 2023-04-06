def num_check(user_num):
    num = user_num
    try:
        num = int(num)
    except:
        num = num_check(input("Вы вместо числа ввели строку. Введите число: "))
    return num

n = num_check(input("Введите кол-во элементов: "))
a1 = num_check(input("Введите первый элемент: "))
d = num_check(input("Введите множитель: "))
a = []
for i in range(n):
    a.append(a1 + i * d)
print(a)

top = num_check(input("Введите верхний предел: "))
bottom = num_check(input("Введите нижний предел: "))
match = []
for i in range(n):
    if top <= a[i] <= bottom:
        match.append(a[i])
print(match)