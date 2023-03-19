a = int(input('км за первый день: '))
b = int(input('км нужно: '))
print(f'1-й день: {a}')
i = 1
while a < b:
    i += 1
    a += round(a * 0.1, 2)
    print(f'{i}-й день: {round(a, 2)}')
print(f'на {i}-й день спортсмен достиг результата — не менее {b} км.')
