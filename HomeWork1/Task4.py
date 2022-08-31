#Задача 4: Напишите программу, которая принимает на вход три числа
# и выдаёт максимальное из этих чисел.

number1 = int(input('Enter number1: '))
number2 = int(input('Enter number2: '))
number3 = int(input('Enter number3: '))
max = number1

if number2 > max:
    max = number2

if number3 > max:
    max = number3

print(max)