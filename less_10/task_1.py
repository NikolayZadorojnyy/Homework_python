"""
Каждое из слов «разработка», «сокет», «декоратор» представить
в буквенном формате и проверить тип и содержание соответствующих переменных.
Затем с помощью онлайн-конвертера преобразовать
в набор кодовых точек Unicode (НО НЕ В БАЙТЫ!!!)
и также проверить тип и содержимое переменных.

*Попытайтесь получить кодовые точки без онлайн-конвертера!
без хардкода!

Подсказки:
--- 'разработка' - буквенный формат
--- '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430' - набор кодовых точек
--- используйте списки и циклы, не дублируйте функции
"""

s_lst = ['разработка', 'сокет', 'декоратор']
for el in s_lst:
    print('переменная - {}'.format(el), '| тип: {}'.format(type(el)))
print('Список строк -', s_lst, '| тип: ', type(s_lst), '\n')

s_u = [u'\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
       u'\u0441\u043e\u043a\u0435\u0442',
       u'\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440']
for el in s_u:
    print('набор кодовых точек - {}'.format(el), '| тип: {}'.format(type(el)))
print('Список строк -', s_u, '| тип: ', type(s_u))
