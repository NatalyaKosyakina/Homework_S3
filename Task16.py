# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

import random

number_n = int(input("Введите число: "))

array = list()
for i in range(number_n):
    array.append(random.randint(1, number_n+10))
print(array)

find_x = int(input("Какое число мы ищем?  "))
count = 0
for j in range(len(array)):
    if array[j] == find_x :
        count += 1

print(' -> ', count)