"""
Написать программу которая проверяет что в строке есть хотя бы один пробел, число,
буква нижнего и верхнего регистра. Если это так, то вывести 'YES', иначе 'NO'
"""

test_string = input("Введите строку: ")

if (any(symbol.isupper() for symbol in test_string)
    and any(symbol.islower() for symbol in test_string)
    and any(symbol.isdigit() for symbol in test_string)
    and any(symbol.isspace() for symbol in test_string)):
    print("Yes")
else:
    print("No")
