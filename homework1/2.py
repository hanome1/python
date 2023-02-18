user_seconds = int(input('input time in seconds: '))
hours = user_seconds // 3600
minutes = user_seconds % 3600 // 60
seconds = user_seconds % 3600 % 60
print(f'{hours}:{minutes}:{seconds}')