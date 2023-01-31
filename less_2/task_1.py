"""
Спортсмен занимается ежедневными пробежками.
В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня,
на который результат спортсмена составит не менее b километров.
Программа должна принимать значения параметров a и b
и выводить одно натуральное число — номер дня.

Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22
Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
"""
a = int(input("Введите положительное число a: "))
b = int(input("Введите положительное число b, большее чем a: "))
if b > a > 0 and b > 0:
    print("1-й день:", a)
    day = 0
    while b - a > 0:
        a = a + a * 0.1
        day += 1
        print(f"{day + 1}-й день: {round(a, 2)}")

    print(f"на {day + 1} день спортсмен достиг результата — не менее {b} км.")
else:
    print("Введены некорректные данные")
