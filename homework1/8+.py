n = int(input('количество долек с одной стороны шоколадки: '))
m = int(input('количество долек с другой стороны шоколадки: '))
k = int(input('сколько долек ты хочешь отломить? '))
if n % k == 0 or m % k == 0:
    print('получится')
else:
    print('не получится')