"""
Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате
чч:мм:сс.
Используйте форматирование строк.

Пример:
Введите время в секундах: 3600
Время в формате ч:м:с - 1.0 : 60.0 : 3600
"""

sec = int(input("Введите время в секундах: "))
hour = float(sec // 3600)
minut = float(sec // 60)

print(f"Время в формате ч:м:с - {hour} : {minut} : {sec}")
