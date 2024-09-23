# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. Функция возвращает
# кортеж из трёх элементов: путь, имя файла, расширение файла.
import os.path


def file_location(link: str) -> tuple:
    directory, file_path = os.path.split(link)
    file_name, extension = file_path.split('.')
    return directory,file_name, extension

x = 'D:\Documents\Francaise\Cinq sur cinq manuel.pdf'
print(file_location(x))