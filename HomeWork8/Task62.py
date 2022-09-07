# Задача 62. Напишите программу,
# которая заполнит спирально массив 4 на 4.

from PrintMatrix import print2D

n = int(input('Enter Maxtix size: '))


def fillmatrix(n):
    """
    Функция создаёт и заполняет матрицу спирально.
    :param n: - задаёт размер матрицы
    :return: - ничего не возвращаем
    """
    matrix = [[0 for j in range(n)] for i in range(n)]
    a = 1
    i = 0
    j = 0
    count = 0
    while (matrix[(i + 1)][j] == 0 or matrix[(i - 1)][j] == 0 or matrix[i][(j + 1)] == 0
           or matrix[i][(j - 1)] == 0 or matrix[i][j] == 0):
        while i < (n - count):  # строка направо
            matrix[j][i] = a
            a += 1
            i += 1
        i -= 1
        j += 1
        while j < (n - count):  # столбец вниз
            matrix[j][i] = a
            a += 1
            j += 1
        i -= 1
        j -= 1
        while i >= (0 + count):  # строка налево
            matrix[j][i] = a
            a += 1
            i -= 1
        i += 1
        j -= 1
        count += 1
        while j >= (0 + count):  # столбец вверх
            matrix[j][i] = a
            a += 1
            j -= 1
        i += 1
        j += 1
    return matrix


matrix = fillmatrix(n)
print2D(matrix)
