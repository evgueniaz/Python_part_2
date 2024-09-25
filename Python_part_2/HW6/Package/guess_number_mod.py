# Ex2
#
from random import randint as rnd
from sys import argv

__all__ = ['guess_num']

def guess_num(low_lim: int = 0, up_lim: int = 100, counter: int = 10) -> bool:
    guess = rnd(low_lim, up_lim)
    for _ in range(counter):
        number = int(input('Try to guess! Enter a whole number:  '))
        if number < guess:
            print(f'The hidden number is greater.')
        elif number > guess:
            print(f'The hidden number is smaller.')
        else:
            print(f'Congratulation! You have guessed!')
            return True
    print(f'Sorry, you havn\'t guessed. Your attempts are over.')
    return False

if __name__ == '__main__':
    param = argv[1 : 4]
    guess_num(*(int(item) for item in param))

