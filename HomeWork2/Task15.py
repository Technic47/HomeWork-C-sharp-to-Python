# Задача 15: Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день

number = int(input('Enter number: '))

if (number > 0) and (number < 8):
    if number > 6:
        print('This is a weekend.')
    else:
        print('This is a working day.')
else:
    print('There is no weekday for your number')