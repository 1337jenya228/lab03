import random as rnd

N = int(input("Введите количество чисел:"))
choise = int(input("Какую сортировку выбираете? 1 - по возрастанию 2 - по убыванию\n"))
while choise != 1 and choise !=2:
    choise = int(input("Какую сортировку выбираете? 1 - по возрастанию 2 - по убыванию\n"))

a = []
for i in range(N):
    a.append(rnd.randint(1, 99))
print(a)

if(choise == 1):
    for i in range(N - 1):
        for j in range(N - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
else:
    for i in range(N - 1):
        for j in range(N - i - 1):
            if a[j] < a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

print(a)