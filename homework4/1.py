list1 = [int(a) for a in input("Введите числа первого множества через пробел: ").split()]
list2 = [int(a) for a in input("Введите числа второго множества через пробел: ").split()]
list_match = list()
for i in range(len(list1)):
    for j in range(len(list2)):
        if list1[i] == list2[j]:
            list_match.append(list1[i])
list_match.sort(reverse=0)
print(set(list_match))