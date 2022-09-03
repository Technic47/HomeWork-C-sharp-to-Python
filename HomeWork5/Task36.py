# Задача 36: Задайте одномерный массив,
# заполненный случайными числами.
# Найдите сумму элементов, стоящих на нечётных позициях.

import random

length = int(input('Enter array length '))
array = []
sum = 0

for i in range(length):
    array.append(random.randint(0, 10))
    if i % 2 == 0:
        sum += array[i]

print(array)
print(f"Sum of numbers with uneven index: {sum}")