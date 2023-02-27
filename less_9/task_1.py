"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность),wage (зарплата), bonus (премия)

Создать не менее двух дескрипторов для атрибутов классов, которые вы создали ранее в ДЗ
"""


class WriteRule:  # дескриптор 1
    def __set__(self, instance, value):
        if type(value) != str:
            raise TypeError(f'Поле {self.my_attr} должно быть строкой!')
        elif not value:
            raise ValueError(f'{self.my_attr} значение обязательно!')
        elif not value.istitle():
            raise ValueError(f'Поле {self.my_attr} записывается с заглавной буквы!')
        elif not len(value) < 20:
            raise ValueError(f'Поле {self.my_attr} должно быть меньше 20 символов!')

        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class NumericRule:  # дескриптор 2
    def __set__(self, instance, value):
        if type(value) not in (int, float):
            raise TypeError(f'{self.my_attr} должно быть числом!')
        elif value < 0:
            raise ValueError(f'{self.my_attr} только положительное число!')

        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Worker:
    name = WriteRule()
    surname = WriteRule()
    position = WriteRule()
    wage = NumericRule()
    bonus = NumericRule()

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus


class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_full_salary(self):
        return self.wage + self.bonus

    def __str__(self):
        return f"Краткое досье: {self.get_full_name()}, {self.position}, месячный доход: {self.get_full_salary()} $"


v_pupkin = Position('Вася', 'Пупкин', 'Суперзвезда', 1000000, 500000)
Shtirlitzh = Position('Максим', 'Исаев', 'Шпион', 122, 0)
print(f'Встречайте: {v_pupkin.name}, {v_pupkin.surname}, {v_pupkin.position}, {v_pupkin.get_full_salary()}')
print(f'{v_pupkin.get_full_name()} - самая высокооплачиваемая звезда России с доходом: {v_pupkin.get_full_salary()} $')
print(v_pupkin)
print(Shtirlitzh)
