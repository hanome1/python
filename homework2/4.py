user_arr = input('Введите целые числа через пробел: ')
arr = user_arr.split()
i = 0
while i < len(arr):
    arr[i] = int(arr[i])
    i+=1
i = 0
while i < len(arr):
    if i + 1 >= len(arr):
        break
    temp = arr[i]
    arr[i] = arr[i+1]
    arr[i+1] = temp
    i+=2
print(f'modified array: {arr}')
