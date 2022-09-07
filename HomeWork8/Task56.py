# Задача 56: Задайте прямоугольный двумерный массив.
# Напишите программу, которая будет находить строку
# с наименьшей суммой элементов.

from random import randint
from PrintMatrix import print2D

n = int(input('Enter N: '))
m = int(input('Enter M: '))

matrix = [[randint(0, 9) for j in range(n)] for i in range(m)]


def sumline(matrix):
    """
    Функция суммирует каждую строчку матрицы - аргумента
    и заносит сумму строки в ячейку массива sums[].
    Выводит в консоль сумму элементов для каждой строки по индексу.
    :param matrix: - матрица для обработки
    :return: - возвращает массив с вычесленными суммами
    """
    sums = []
    for i in range(len(matrix)):
        sum = 0
        for j in range(len(matrix[i])):
            sum += matrix[i][j]
        print(f'Sum in {i} = {sum}')
        sums.append(sum)
    return sums


def minsum(sums):
    """
    Функция находит минимальное значение из массива
    и выводит его в консоль.
    :param sums: - массив для поиска
    :return: - ничего не возвращаем
    """
    min = sums[0]
    for i in range(len(sums)):
        if sums[i] < min:
            min = sums[i]
            index = i
    print(f'Index of min sum = {min} line is {index}.')


print2D(matrix)
print()
sums = sumline(matrix)
print()
minsum(sums)
