# Задача 8: Напишите программу, которая на вход принимает число (N),
# а на выходе показывает все чётные числа от 1 до N.

number1 = int(input('Enter number: '))
index = 0

while index <= number1:
    if index % 2 == 0:
        print(index)
    index += 1
