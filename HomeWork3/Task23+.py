# Напишите программу, которая принимает на вход число (N)
# и выдаёт таблицу кубов чисел, которые не более N.

number = int(input('Enter number: '))
array = []

for i in range(number + 1):
    x = i ** 3
    if x < number:
        array.append(x)
    else:
        break

print(array)