# Ex1
#
# Задание 1
# создание из файла txt нового файла json
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.
# '''

__all__ = ['txt_to_json']


import json
from pathlib import Path

def txt_to_json(txt_file: str, json_file: str):
    with (open (txt_file, 'r', encoding='utf-8') as fin,      #открываем  файл dataset.txt считываем в словарь my_dict
        open(json_file, "w", encoding='utf-8') as fout):      # создаем  dataset.json
        contents = fin.readlines()
        my_dict = {}
        for line in contents:                                   # данные из dataset.txt считываем в словарь my_dict
            key, val = line.split()
            my_dict[key.title()] = float(val)

        json.dump(my_dict, fout, separators=(',\n', ':'))        #запись в  dataset.json словаря my_dict

if __name__ == '__main__':
    txt_to_json(Path('dataset.txt'), Path('dataset.json'))