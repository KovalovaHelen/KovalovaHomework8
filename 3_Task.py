"""
Напишите программу где пользователь вводит пароль,
а программа проверяет сложность пароля и выводит свой результат в оценочной шкале от 1 до 5.
1 - у пользователя пароль == 'qwerty' or 'admin' или пароль пустой
2 - у пользователя только цифры или спец. символы или все буквы в верхнем или нижнем регистре
3 - у пользователя есть буквы в (нижнем или верхнем регистре) и цифры
4 - у пользователя есть цифры, буквы нижнего и верхнего регистра
5 - у пользователя есть цифры, буквы нижнего и верхнего регистра, спец. символы и длинна пароля больше 8 символов
"""

password = input('Give me your password: ')

has_digit = False
has_upper = False
has_lower = False
has_spec = False


if not password or password == 'admin' or password == 'qwerty':
    print('Level 1')
    exit()

for char in password:
    if char.isdigit():
        has_digit = True
    elif char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    else:
        has_spec = True

correct_length = len(password) > 8
total_result = has_digit + has_upper + has_lower + has_spec

if total_result == 1:
    print('Level 2')
elif total_result == 2:
    print('Level 3')
elif total_result >= 3 and not correct_length:
    print('Level 4')
elif total_result == 4 and correct_length:
    print('Level 5')
