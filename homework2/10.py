import random
n = int(input('Введите количество монет: '))
count = 0
for i in range(n):
    x = random.randint(0, 1)
    if x == 0:
        count += 1
print(f'орлом вверх: {count}\nрешкой вверх: {n - count}')
if count < n - count:
    print (f'нужно перевернуть {count} монет')
else:
    print (f'нужно перевернуть {n - count} монет')