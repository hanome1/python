nums = int(input('input some nums: '))
max = nums % 10
while nums > 0:
    nums //= 10
    if nums % 10 > max:
        max = nums % 10
print(f'max num is {max}')