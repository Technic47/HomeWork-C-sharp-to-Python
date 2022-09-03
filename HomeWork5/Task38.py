# Задача 38: Задайте массив вещественных чисел.
# Найдите разницу между максимальным и минимальным элементов массива.

import random

length = int(input('Enter array length '))
array = []
sum = 0

for i in range(length):
    array.append((random.randint(-10000, 10000)/100))

maxx = max(array)
minn = min(array)

diff = maxx - minn
round(diff, 2)
print(array)
print('Maximum number: {}\nMinimum number : {}\nDifference is: {}'.format(maxx, minn, diff))