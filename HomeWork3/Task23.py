# Напишите программу, которая принимает на вход число (N)
# и выдаёт таблицу кубов чисел

number = int(input('Enter number: '))
array = []

for i in range(number + 1):
    x = i ** 3
    array.append(x)

print(array)