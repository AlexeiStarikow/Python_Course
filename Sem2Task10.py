# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

num=int(input("Введите количество монет: "))

one=0
zero=0

for i in range(num):
    x=int(input("Орел 1/Решка 0: "))
    if x==0:
        zero+=1
    else:
        one+=1

if one>zero:
    print(zero)
else:
    print(one)