# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной
# расстановки ферзей в задаче выше. Проверяйте различный случайные варианты и выведите
# 4 успешных расстановки.


from Package import check_queens
import random

def gen_list() -> list[tuple[int, int]]:
    list_of_pos = []
    while len(list_of_pos) < 9:
        x, y = random.randint(1, 8), random.randint(1, 8)
        if (x, y) not in list_of_pos:
            list_of_pos.append((x, y))
    return list_of_pos

def find_success_pos():
    count = 0
    while count < 4:
        data = gen_list()
        while not check_queens.check_queens(data):
            data = gen_list()
        else:
            count += 1
            print(data)


if __name__ == '__main__':
    find_success_pos()
