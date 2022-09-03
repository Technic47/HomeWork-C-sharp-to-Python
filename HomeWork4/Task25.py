# Напишите цикл, который принимает на вход два числа (A и B)
# и возводит число A в натуральную степень B.

number1 = int(input('Enter number1: '))
number2 = int(input('Enter number2: '))


def deg(a):
    deg = 1
    for i in range(a):
        deg *= number1
    return deg


print(deg(number2))
