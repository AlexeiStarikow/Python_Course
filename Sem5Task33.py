# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

from random import randint
n = int(input("Количество оценок в журнале: "))
list_1 = [randint(1, 5) for _ in range(n)]
print(*list_1)
max_ocenka = max(list_1)
min_ocenka = min(list_1)
print(max_ocenka)
print(min_ocenka)

for i in range(n):
    if list_1[i]==max_ocenka:
        list_1[i]=min_ocenka
print(list_1)