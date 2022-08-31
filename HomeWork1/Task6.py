#Задача 6: Напишите программу, которая на вход принимает число
# и выдаёт, является ли число чётным (делится ли оно на два без остатка).

number1 = int(input('Enter number1: '))

dev = number1 % 2

if dev == 0:
    print('True')
else:
    print('False')