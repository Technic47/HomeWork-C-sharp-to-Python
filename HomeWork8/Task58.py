# Задайте две матрицы. Напишите программу,
# которая будет находить произведение двух матриц.

from random import randint
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
a = np.array(matrix1)
b = np.array(matrix2)

def printmatrix(matrix):
    print()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
        print()


def arraymultiplication(matrix1, matrix2):
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


printmatrix(matrix1)
printmatrix(matrix2)
matrix3 = arraymultiplication(matrix1, matrix2)
printmatrix(matrix3)
print()
total = a.dot(b)
print(total)
