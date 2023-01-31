"""
Создать список и заполнить его элементами различных типов данных.
Реализовать проверку типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

Пример:
для списка [5, "string", 0.15, True, None]
результат

<class 'int'>
<class 'str'>
<class 'float'>
<class 'bool'>
<class 'NoneType'>
"""
a = [10, "Hello", 100.0, True, None, {1:'value', 'key':2}, {5,2,3,1,4}, [5,10,15], (5,'program', 1+3j), 1+2j]

print(type(a[0]))
print(type(a[1]))
print(type(a[2]))
print(type(a[3]))
print(type(a[4]))
print(type(a[5]))
print(type(a[6]))
print(type(a[7]))
print(type(a[8]))
print(type(a[9]))