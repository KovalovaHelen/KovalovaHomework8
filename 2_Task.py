"""
Напишите программу где пользователь вводит число - count, а программа выводит count чисел фибоначчи.
"""

f1 = f2 = 1

count = int(input("Введите число: "))
print("0", f1, f2, end=" ")

for i in range(2, count):
    f1, f2 = f2, f1 + f2
    print(f2, end=" ")
