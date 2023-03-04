user_arr = input('Введите слова через пробел: ')
arr = user_arr.split()
i = 0
while i < len(arr):
    print(f'{i+1}. {arr[i][:10]}')
    i+=1

