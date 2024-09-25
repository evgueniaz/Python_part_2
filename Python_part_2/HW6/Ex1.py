# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

from Package import year_mod
from sys import argv

def date_terminal():
    date = argv[1]
    print(year_mod.date_is_true(date))

if __name__ == '__main__':
    date_terminal()