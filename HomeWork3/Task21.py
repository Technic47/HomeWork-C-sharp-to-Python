# Задача 21 Напишите программу,
# которая принимает на вход координаты двух точек
# и находит расстояние между ними в 3D пространстве.

print('Write x y z coordinates for A')
x1 = int(input('X: '))
y1 = int(input('Y: '))
z1 = int(input('Z: '))

print('Write x y z coordinates for B')
x2 = int(input('X: '))
y2 = int(input('Y: '))
z2 = int(input('Z: '))

A = [x1, y1, z1]
B = [x2, y2, z2]


def SqrSum(a):
    result = (B[a] - A[a]) ** 2
    return result

dist = (SqrSum(0) + SqrSum(1) + SqrSum(2)) ** 0.5

print(dist)
