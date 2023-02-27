"""
Реализовать класс Road (дорога), в котором определить атрибуты:
 length (длина), width (ширина). Значения данных атрибутов должны
 передаваться при создании экземпляра класса. Атрибуты сделать
 защищенными. Определить метод расчета массы асфальта, необходимого
 для покрытия всего дорожного полотна. Использовать формулу: длина
 * ширина * масса асфальта для покрытия одного кв метра дороги
 асфальтом, толщиной в 1 см * число см толщины полотна. Массу и
 толщину сделать публичными атрибутами.

Создать метакласс для паттерна Синглтон
"""


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Road(metaclass=Singleton):
    # удельная масса 1кв.м. дорожного полотна толщиной 1 см (тонн)
    _surface_spec_gravity: float = 0.025

    def __init__(self, length: float, width: float, thickness: float):
        self._length = float(length)
        self._width = float(width)
        self._thickness = float(thickness)  # толщина покрытия в метрах

    def get_surface_gravity(self):
        return (self._length * self._width
                * self._thickness * self._surface_spec_gravity)


road = Road(5000, 20, 0.05)
road1 = Road(1000, 10, 0.01)
# ссылки на объекты одинаковые
print('Патерн Singleton => объект 1 равен объекту 2?:', road == road1)
print('Масса:', road.get_surface_gravity(), 'тонн', 'Ссылка на объект 1:', road)
print('Масса:', road1.get_surface_gravity(), 'тонн', 'Ссылка на объект 2:', road1)


class Road1:
    # удельная масса 1кв.м. дорожного полотна толщиной 1 см (тонн)
    _surface_spec_gravity: float = 0.025

    def __init__(self, length: float, width: float, thickness: float):
        self._length = float(length)
        self._width = float(width)
        self._thickness = float(thickness)  # толщина покрытия в метрах

    def get_surface_gravity(self):
        return (self._length * self._width
                * self._thickness * self._surface_spec_gravity)


road = Road1(5000, 20, 0.05)
road1 = Road1(1000, 10, 0.01)
# ссылки на объекты разные
print('Без патерна Singleton => объект 1 равен объекту 2?:', road == road1)
print('Масса:', road.get_surface_gravity(), 'тонн', 'Ссылка на объект 1:', road)
print('Масса:', road1.get_surface_gravity(), 'тонн', 'Ссылка на объект 2:', road1)
