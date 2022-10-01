"""
Напишите программу где пользователь вводит пароль,
а программа проверяет сложность пароля и выводит свой результат в оценочной шкале от 1 до 5.
1 - у пользователя пароль == 'qwerty' or 'admin' или пароль пустой
2 - у пользователя только цифры или спец. символы или все буквы в верхнем или нижнем регистре
3 - у пользователя есть буквы в (нижнем или верхнем регистре) и цифры
4 - у пользователя есть цифры, буквы нижнего и верхнего регистра
5 - у пользователя есть цифры, буквы нижнего и верхнего регистра, спец. символы и длинна пароля больше 8 символов
"""

password = input("Введите пароль: ")

if password == "qwerty" or password == "admin" or password == " ":
    print("Оценка пароля 1")
elif password.isupper() or password.islower() or password.isdigit():
    print("Оценка пароля 2")
elif password.isupper() or password.islower() and password.isdigit():
    print("Оценка пароля 3")
elif password.isupper() and password.islower() and password.isdigit():
    print("Оценка пароля 4")
elif len(password) > 8 and password.isupper() and password.islower() and password.isdigit():
    print("Оценка пароля 5")
else:
    exit()

