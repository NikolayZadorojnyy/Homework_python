"""
Задайте натуральное число N. Напишите программу, которая составит список
простых множителей числа N.
"""

num = int(input("Введите натуральное число: "))
list_simple = []
simple = 2
while num > 1:
    if num % simple == 0:
        list_simple.append(simple)
        num = num/simple
    else:
        simple += 1
print("Простые множители:",list_simple)