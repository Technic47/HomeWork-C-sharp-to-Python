# Задача 60. ...Сформируйте трёхмерный массив
# **из неповторяющихся** двузначных чисел.
# Напишите программу, которая будет построчно выводить массив,
# добавляя индексы каждого элемента.
import random

from PrintMatrix import print3D

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

matrix = creatematrix(n, m, p)
print3D(matrix)
