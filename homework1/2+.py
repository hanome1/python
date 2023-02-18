num = int(input('input your number: '))
sum_digits = 0
while num > 0:
    sum_digits += num % 10
    num //= 10
print(f'sum of your number\'s digits is {sum_digits}')