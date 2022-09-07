# Задача 54: Задайте двумерный массив.
# Напишите программу, которая упорядочит по убыванию
# элементы каждой строки двумерного массива.

from random import randint

n = int(input('Enter N: '))
m = int(input('Enter M: '))

matrix = [[randint(0, 9) for j in range(n)] for i in range(m)]

def printmatrix(matrix):
    """
    Функция вывода 2х - мерного массива в консоли.
    :param matrix: - исходная матрица (массив)
    :return: - ничего не возвращаем
    """
    print()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
        print()

def sortmatrix(matrix):
    """
    Функция для сортировки матрицы по убыванию
    :param matrix: - матрица для сортировки
    :return: - ничего не возвращаем
    """
    for i in range(len(matrix)):
        matrix[i].sort(reverse=True)

printmatrix(matrix)
sortmatrix(matrix)
printmatrix(matrix)


