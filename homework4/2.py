berries = [int(a) for a in input("Введите количество ягод на каждом кусте через пробел: ").split()]
grabber = list()
for i in range(len(berries)-1):
    grabber.append(berries[i-1] + berries[i] + berries[i+1])
grabber.append(berries[len(berries)-2] + berries[len(berries)-1] + berries[0])
print(max(grabber))