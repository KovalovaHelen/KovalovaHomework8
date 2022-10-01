"""
Напишите программу где пользователь вводит число symbol_len, а программа генерирует пароль длинной symbol_len.
Чем выше будет сложность пароля, тем лучше. Сложность пароля буду оценивать по шкале от 1 до 5 из задании #3
"""

import random

bukva1 = "qwertyuiopasdfghjklzxcvbnm"
bukva2 = bukva1.upper()
digit = "0123456789"
znak = "!@#$%^&*()_+"
elements = bukva1 + bukva2 + digit + znak

symbol_len = int(input("Введите длину пароля: "))
password = ""

if symbol_len <= 8:
    print("Слабый пароль")
elif symbol_len > 8:
    password = ''.join([random.choice(elements) for x in range(symbol_len)])

print(password)
