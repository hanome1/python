from timeit import timeit

m = [int(a) for a in input("Введите числа первого множества через пробел: ").split()]
n = [int(a) for a in input("Введите числа второго множества через пробел: ").split()]
def solution(list1, list2):
    list_match = list()
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                list_match.append(list1[i])
    list_match.sort(reverse=0)
    print(set(list_match))
solution(m, n)
print(timeit("solution()", m, n, globals=globals(), number=1000))