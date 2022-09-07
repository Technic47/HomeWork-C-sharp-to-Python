# Задача 60. ...Сформируйте трёхмерный массив
# **из неповторяющихся** двузначных чисел.
# Напишите программу, которая будет построчно выводить массив,
# добавляя индексы каждого элемента.
import random

n = int(input('Enter Maxtix N: '))
m = int(input('Enter Maxtix M: '))
p = int(input('Enter Maxtix P: '))


def creatematrix(n, m, p):
    """
    Функция генерирует 3х мерный массив
    заполненный рандомными числами от 0 до 9
    :param n: - количество строк
    :param m: - количество столбцов
    :param p: - количество 3их ячеек для 3Д массива
    :return:  - возвращаем матрицу
    """
    matrix = []
    for i in range(n):
        a = []
        for j in range(m):
            b = []
            for k in range(p):
                b.append(random.randint(0, 9))
            a.append(b)
        matrix.append(a)
    return matrix


def printmatrix3D(matrix):
    """
    Функция вывода 3х - мерного массива в консоли.
    :param matrix: - исходная матрица (массив)
    :return: - ничего не возвращаем
    """
    for i in range(n):
        for j in range(m):
            for k in range(p):
                print(f'{matrix[i][j][k]} [{i}, {j}, {k}]')


matrix = creatematrix(n, m, p)
printmatrix3D(matrix)
