#  Задача 47. Задайте двумерный массив размером m×n,
# заполненный случайными вещественными числами.
from random import randint
from PrintMatrix import print2D

n = int(input('Enter N: '))
m = int(input('Enter M: '))

matrix = [[randint(0, 9) for j in range(m)] for i in range(n)]

print2D(matrix)