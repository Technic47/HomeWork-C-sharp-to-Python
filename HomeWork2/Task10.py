#Задача 10: Напишите программу,
#которая принимает на вход трёхзначное число
#и на выходе показывает вторую цифру этого числа.

number = int(input('Enter 3-digit number: '))
number1 = number
ost = 1
array = list()

while ost != 0:
    number1 /= 10;
    ost = number1 % 10
