# Задача 34: Задайте массив заполненный случайными
# положительными трёхзначными числами.
# Напишите программу, которая покажет количество чётных чисел
# в массиве.

import random

length = int(input('Enter array length '))
array = []
count = 0

for i in range(length):
    array.append(random.randint(0, 10))
    if array[i] % 2 == 0:
        count +=1

print(array)
print(count)
