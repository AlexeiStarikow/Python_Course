# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

from random import randint

n=int(input("Введите длину списка: "))
a=int(input("Введите нижнюю границу диапазона: "))
b=int(input("Введите верхнюю границу диапазона: "))

list_1=[randint(1,10) for i in range(n)]

list_ind=[]

for i in range(len(list_1)):
    if a<=list_1[i]<=b:
        list_ind.append(i)

print(list_1)
print(list_ind)