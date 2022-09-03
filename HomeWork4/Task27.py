# Напишите программу, которая принимает на вход число
# и выдаёт сумму цифр в числе.

number = int(input('Enter number: '))


def sumnum(a):
    ost = 0
    sum = 0
    while a != 0:
        ost = a % 10
        sum += ost
        a //= 10
    return sum


print(sumnum(number))
