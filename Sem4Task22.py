# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

n=int(input("Введите количество элементов первого множества: "))
m=int(input("Введите количество элементов второго множества: "))

list_n = []
for i in range(n):
    list_n.append(int(input("Введите элемент первого множества: ")))

list_m = []
for i in range(m):
    list_m.append(int(input("Введите элемент второго множества: ")))

print(list_n)
print(list_m)

set_n=set(list_n)
set_m=set(list_m)

print(set_n)
print(set_m)

set_1=set_n.intersection(set_m)
print(set_1)