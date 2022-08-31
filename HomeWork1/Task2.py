#Задача 2: Напишите программу, которая на вход принимает два числа
# и выдаёт, какое число большее, а какое меньшее.

number1 = input('Enter number1: ')
number2 = input('Enter number2: ')
max = number1

if number2 > number1:
    max = number2

print(max)

