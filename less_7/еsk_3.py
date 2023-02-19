"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"profit": profit, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_full_profit).
Проверить работу примера на реальных данных (создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:

    def __init__(self, name='', surname='', position='', wage=0, bonus=0):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'зарплата': wage, 'премия': bonus}


class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_full_salary(self):
        return self._income['зарплата'] + self._income['премия']

    def __str__(self):
        return f"Краткое досье: {self.get_full_name()}, {self.position}, месячный доход: {self.get_full_salary()} $"


v_pupkin = Position('Вася', 'Пупкин', 'Суперзвезда', 1000000, 500000)
Shtirlitzh = Position('Максим', 'Исаев', 'Шпион', 1000, 0)
print(f'Встречайте: {v_pupkin.name}, {v_pupkin.surname}, {v_pupkin.position}, {v_pupkin._income}')
print(f'{v_pupkin.get_full_name()} - самая высокооплачиваемая звезда России с доходом: {v_pupkin.get_full_salary()} $')
print(v_pupkin)
print(Shtirlitzh)
