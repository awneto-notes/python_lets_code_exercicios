import random

lista = []

for i in range(random.randint(1,100)):
    lista.append(random.randint(1,100))

print(lista)

count = 0
for item in lista:
    if item % 2 == 0:
        count += 1

print(count)