# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

import random
import math

number_n = int(input("Введите число: "))

array = list()
for i in range(number_n):
    array.append(random.randint(1, number_n+10))
print(array)

find_x = int(input("На какое число мы ориентируемся?  "))

dif_f = abs(find_x - array[0])
near_x = 0
for i in range(len(array)):
    if  abs(find_x - array[i]) < dif_f :
        dif_f = abs(find_x - array[i])
        near_x = array[i]

print(" -> ", near_x)