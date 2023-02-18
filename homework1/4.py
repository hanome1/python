profit = int(input('Введите выручку фирмы: '))
costs = int(input('Введите издержки фирмы: '))
if profit > costs:
    print(f'Финансовый результат - прибыль. Ее величина: {profit - costs}')
else:
    print(f'Финансовый результат - убыток. Его величина: {costs - profit}')
print(f'Рентабельность выручки: {(profit - costs) / profit}')
people = int(input('Введите численность сотрудников фирмы: '))
print(f'Прибыль фирмы в расчете на одного сотрудника: {(profit - costs) / people}')