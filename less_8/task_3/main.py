"""
3. Задание на закрепление знаний по модулю yaml.
 Написать скрипт, автоматизирующий сохранение данных
 в файле YAML-формата.
Для этого:

Подготовить данные для записи в виде словаря, в котором
первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа —
это целое число с юникод-символом, отсутствующим в кодировке
ASCII(например, €);

Реализовать сохранение данных в файл формата YAML — например,
в файл file.yaml. При этом обеспечить стилизацию файла с помощью
параметра default_flow_style, а также установить возможность работы
с юникодом: allow_unicode = True;

Реализовать считывание данных из созданного файла и проверить,
совпадают ли они с исходными.
"""
import yaml


def yaml_save_data():  # запись в файл
    my_data = {
        'items': ["table", "chair", "closet", "mirror", "sofa"],
        'items_ptice': {
            'table': '200\u20AC-1000\u20AC',
            'chair': '10\u20AC-100\u20AC',
            'closet': '100\u20AC-500\u20AC',
            'mirror': '10\u20AC-50\u20AC',
            'sofa': '1000\u20AC-3000\u20AC'
        },
        'items_quantity': 5
    }

    with open('homework_8.3.yaml', 'w', encoding='utf-8') as yaml_file:
        yaml.dump(my_data, yaml_file, default_flow_style=False, allow_unicode=True)


def read_yaml_file():  # считывание файла
    try:
        with open('homework_8.3.yaml', 'r', encoding='utf-8') as f_n:
            print(f_n.read())
    except FileNotFoundError:
        print('файла не существует')


yaml_save_data()
read_yaml_file()
