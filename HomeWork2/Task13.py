# Задача 13: Напишите программу,
# которая выводит третью цифру заданного числа или сообщает,
# что третьей цифры нет.

number = input('Enter number: ')
length = len(number)
array = []
number = int(number)
for i in range(length):
    ost = number % 10
    number //= 10
    array.append(ost)
if len(array) < 3:
    print('There is no 3rd digit in your number!')
else:
    print(array[-3])
    print(len(array))