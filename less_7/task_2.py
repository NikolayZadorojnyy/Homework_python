"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color
    (цвет) и метод running (запуск). Атрибут реализовать как приватный.
    В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
    Продолжительность первого состояния (красный) составляет 7 секунд, второго
    (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
    Переключение между режимами должно осуществляться только в указанном порядке
    (красный, желтый, зеленый).
    Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""
from time import sleep


class TrafficLight:
    _states = {'красный': 7, 'желтый': 2, 'зеленый': 7}
    _color = ''

    def running(self):
        for color, sw_time in self._states.items():
            self._color = color

            print(f"Включен '{self._color}' сигнал светофора. "
                  f"Время работы {sw_time} секунд.")

            sleep(sw_time)


tl = TrafficLight()
tl.running()