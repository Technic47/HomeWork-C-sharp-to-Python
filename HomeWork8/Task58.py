# Задайте две матрицы. Напишите программу,
# которая будет находить произведение двух матриц.

from random import randint
from PrintMatrix import print2D
import numpy as np


n1 = int(input('Enter Maxtix A (X,..): '))
m1 = int(input('Enter Maxtix A (..,Y): '))
n2 = int(input('Enter Maxtix B (X,..): '))
m2 = int(input('Enter Maxtix B (..,Y): '))

if (n1 != m2) or (n2 != m1):
    print('Incorect Mitrix sizes for multiplication!')
    quit()

matrix1 = [[randint(0, 9) for j in range(n1)] for i in range(m1)]
matrix2 = [[randint(0, 9) for j in range(n2)] for i in range(m2)]
a = np.array(matrix1)  # задание матрицы 1 для модуля numpy
b = np.array(matrix2)  # задание матрицы 2 для модуля numpy


def arraymultiplication(matrix1, matrix2):
    """
    Функция перемножения 2х матриц.
    Подгоняет размер результирующей исходя из
    размеров матриц - множителей.
    :param matrix1: - матрица множитель 1.
    :param matrix2: - матрица множитель .
    :return: - возвращает результирующую матрицу.
    """
    n = len(matrix1)
    m = len(matrix2[0])
    matrix3 = [[0 for j in range(n)] for i in range(m)]
    size = 0
    if len(matrix1) < len(matrix1[0]):
        size = len(matrix1[0])
    else:
        size = len(matrix2)

    for i in range(n):
        for j in range(m):
            for p in range(size):
                matrix3[i][j] += matrix1[i][p] * matrix2[p][j]
    return matrix3


print2D(matrix1)
print2D(matrix2)
matrix3 = arraymultiplication(matrix1, matrix2)
print2D(matrix3)
print()
total = a.dot(b)  # перемножение матриц, используя numpy
print(total)
