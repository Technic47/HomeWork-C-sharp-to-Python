# Задача 52. Задайте двумерный массив из целых чисел.
# Найдите среднее арифметическое элементов в каждом столбце.

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
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
        print()


# print(matrix)

def sumline(matrix):
    """
    Функция для подсчёта среднего арифметического чисел в каждой строке
    Выводит в консоль результаты для каждой строки по индексу
    :param matrix: - матрица для подсчёта
    :return: - ничего не возвращаем
    """
    for i in range(len(matrix)):
        sum = 0
        for j in range(len(matrix[i])):
            sum += matrix[i][j]
        ave = (sum/len(matrix[i]))
        print(f'Average in {i} = {ave}')


printmatrix(matrix)
sumline(matrix)
