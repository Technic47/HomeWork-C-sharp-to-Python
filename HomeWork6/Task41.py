# Задача 41: Пользователь вводит с клавиатуры M чисел.
# Посчитайте, сколько чисел больше 0 ввёл пользователь.

array = list(input("Enter numbers via 'space' ").split())

count = 0
for i in range(len(array)):
    if int(array[i]) > 0:
        count += 1

print(array)
print(f"Count of positive numbers: {count}")
