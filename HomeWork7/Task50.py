# Задача 50. Напишите программу,
# которая на вход принимает позиции элемента в двумерном массиве,
# и возвращает значение этого элемента или же указание,
# что такого элемента нет.

from random import randint

matrix = [[randint(0, 10) for j in range(5)] for i in range(10)]

print(matrix)
print(len(matrix)) # количество строк
print(len(matrix[0])) # количество столбцов

n = int(input('Enter N: '))
m = int(input('Enter M: '))

if n < len(matrix) and m < len(matrix[0]):
    print(matrix[n][m])
else:
    print('Your index is not in range of array!')



