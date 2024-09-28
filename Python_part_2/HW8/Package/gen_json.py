# Ex2

# Задание №2
# Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в
# JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа.
# При перезапуске функции уже записанные в файл данные
# должны сохраняться.
# '''
#
#

__all__ = ['input_user']

from pathlib import Path
import json

def input_user(path: Path) -> None:
    unique_id = set()
    if not path.is_file():
        data = {str(level): {} for level in range(1, 8)}
    else:
        with open(path, 'r', encoding='UTF-8') as f_read:
            data = json.load(f_read)
            # unique_id = {id_name.keys() for id_name in data.values() for id in id_name.keys()}
            for id_name in data.values():
                unique_id.update(id_name.keys())

    while name := input('Enter a user name:  '):
        level = input('Enter an access level from 1 to 7:  ')
        user_id = input('Enter a user id:  ')
        if user_id not in unique_id:
            unique_id.add(user_id)
            data[level].update({user_id: name})
            with open(path, 'w', encoding='UTF-8') as f_write:
                json.dump(data, f_write, indent=4, ensure_ascii=False)
        else:
            print('This user id already exists!')

if __name__ == '__main__':
    input_user(Path('users.json'))

