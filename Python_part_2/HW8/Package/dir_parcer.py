# Условие
# 1. Решить задачи, которые не успели решить на семинаре.
# 2. Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
# 3. Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами разных форматов.

__all__ = ['find_size', 'directory_parcer']


from pathlib import Path
import csv
import json
import pickle
import os

def find_size(path: Path) -> float:
    res = 0
    for dir_path, dir_names, file_names in os.walk(path):
        for el in file_names:
            file_path = os.path.join(dir_path, el)
            res += os.path.getsize(file_path)
    return res

def directory_parcer(dir_path: Path):
    results = []
    for root, dirs, files in os.walk(dir_path):
        for name in files:
            full_path = os.path.join(root, name)
            results.append({"parent_directory": root,
                            "object_type": 'file',
                            "name": name,
                            "size_in_bytes": os.path.getsize(full_path)})

        for name in dirs:
            full_path = os.path.join(root, name)
            results.append({"parent_directory": root,
                            "object_type": 'directory',
                            "name": name,
                            "size_in_bytes": find_size(full_path)})

    with open("results.json", "w") as f_json:
        json.dump(results, f_json, indent=4, ensure_ascii=False)

    with open("results.csv", "w") as f_csv:
        writer = csv.DictWriter(f_csv, fieldnames=results[0].keys(), dialect='excel-tab')
        writer.writeheader()
        writer.writerows(results)

    with open("results.pickle", "wb") as f_pickle:
        pickle.dump(results, f_pickle)



if __name__ == '__main__':
    directory_parcer("D:\Geekbrains\Git_Tasks\Python_part_2")