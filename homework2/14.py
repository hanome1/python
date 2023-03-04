import random
n = int(input('Введите число: '))
for i in range(n):
    i += 1
    if 2 ** i < n: 
        print(2**i)
    else:
        break