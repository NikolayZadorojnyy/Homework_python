"""
Поработайте с переменными, создайте несколько,
выведите на экран, запросите у пользователя несколько чисел и
строк и сохраните в переменные, выведите на экран.
Пример:
Ведите ваше имя: Василий
Ведите ваш пароль: vas
Введите ваш возраст: 45
Ваши данные для входа в аккаунт: имя - Василий, пароль - vas,
возраст - 45
"""
a = 5
b = "Hello World!"
lst = [1, 2, 3]
print(int(a))
print(str(b))
print(lst)
name = str(input("Ведите ваше имя: "))
age = int(input("Ваш возраст? "))
val = int(input("Введите число от 1 до 10 "))
print(name, "в ваши", age, "лет пора знать цифры и побольше")
print(f"Но, {name}, я верю в Вас!")
