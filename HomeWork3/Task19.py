# Напишите программу, которая принимает на вход пятизначное число
# и проверяет, является ли оно палиндромом.

number = input('Enter 5 digit number: ')
length = len(number)
array = []
number = int(number)

if length != 5:
    print("Your number is wrong")
else:
    for i in range(length):
        ost = number % 10
        number //= 10
        array.append(ost)

    if (array[0] == array[-1]) and (array[1] == array[-2]):
        print('True')
    else:
        print('False')