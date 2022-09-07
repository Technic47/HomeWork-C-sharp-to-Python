
def print2D(matrix):
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

def print3D(matrix):
    """
    Функция вывода 3х - мерного массива в консоли.
    :param matrix: - исходная матрица (массив)
    :return: - ничего не возвращаем
    """
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            for k in range(len(matrix[i][j])):
                print(f'{matrix[i][j][k]} [{i}, {j}, {k}]')