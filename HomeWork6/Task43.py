#  Задача 43: Напишите программу,
# которая найдёт точку пересечения двух прямых,
# заданных уравнениями y = k1 * x + b1, y = k2 * x + b2;
# значения b1, k1, b2 и k2 задаются пользователем.

b1 = int(input('Enter b1 '))
k1 = int(input('Enter k1 '))
b2 = int(input('Enter b2 '))
k2 = int(input('Enter k2 '))


def DotX(k1, b1, k2, b2):
    result = ((b2 - b1) / (k1 - k2))
    return result


x = DotX(k1, b1, k2, b2)


def DotY(x, k2, b2):
    result = k2 * x + b2
    return result


y = DotY(x, k2, b2)

print('Crosspoint is [{}, {}]'.format(x, y))
