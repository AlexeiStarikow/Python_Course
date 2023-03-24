# 1 Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.

# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
from random import randint
n=int(input("Введите количество элементов массива: "))
list=[0]*n
for i in range(n):
    list[i]=randint(1,10)
print(list)

i=1
sum=0
for i in range(1,len(list),2):
    sum=sum+list[i]
print(sum)
# или
# my_list = [8, 5, 7, 3, 6]
# print(sum(my_list[1::2]))

# 2. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

num=int(input("Введите количество элементов массива: "))
list=[0]*n
for i in range(num):
    list[i]=randint(1,10)

list_1=[]

for i in range(len(list)):
    while i< len(list)/2 and num>len(list)/2:
        num=num-1
        a=list[i]*list[num]
        list_1.append(a)
        i+=1
print(list)
print(list_1)
