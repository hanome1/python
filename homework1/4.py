profit = int(input('Введите выручку фирмы: '))
costs = int(input('Введите издержки фирмы: '))
if profit > costs:
    print(f'Финансовый результат - прибыль. Ее величина: {profit - costs}')
elif profit < costs:
    print(f'Финансовый результат - убыток. Его величина: {costs - profit}')
else:
    print('Финансовый результат - вышли в ноль')
print(f'Рентабельность выручки: {(profit - costs) / profit}')
people = int(input('Введите численность сотрудников фирмы: '))
print(f'Прибыль фирмы в расчете на одного сотрудника: {(profit - costs) / people}')