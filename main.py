import random as rnd

N = int(input("Введите количество чисел:"))
a = []
for i in range(N):
    a.append(rnd.randint(1, 99))
print(a)

for i in range(N - 1):
    for j in range(N - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print(a)