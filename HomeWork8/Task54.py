# Задача 54: Задайте двумерный массив.
# Напишите программу, которая упорядочит по убыванию
# элементы каждой строки двумерного массива.

from random import randint
from PrintMatrix import print2D

n = int(input('Enter N: '))
m = int(input('Enter M: '))

matrix = [[randint(0, 9) for j in range(n)] for i in range(m)]


def sortmatrix(matrix):
    """
    Функция для сортировки матрицы по убыванию
    :param matrix: - матрица для сортировки
    :return: - ничего не возвращаем
    """
    for i in range(len(matrix)):
        matrix[i].sort(reverse=True)

print2D(matrix)
sortmatrix(matrix)
print2D(matrix)


