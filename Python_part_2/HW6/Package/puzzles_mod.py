# Ex5

__all__ = ['puzzles', 'puzzle_storage']

_data = {}


def puzzles(puzzle: str, answers: list[str], counter: int = 3) -> int:
    print(f'Guess a puzzle!')
    print(f'{puzzle}')
    for i in range(counter):
        answer = input('Enter an answer:  ').lower()
        if answer in answers:
            print('Congratulation! You have guessed!')
            return i + 1
    print(f'Sorry, you havn\'t guessed. Your attempts are over.')
    return 0


def puzzle_storage():
    storage = {
        'Зимой и летом одним цветом': ['ель', 'елка', 'ёлка', 'сосна'],
        'Не лает, не кусает, а в дверь не пускает': ['замок', 'засов', 'задвижка'],
        'Висит груша - нельзя скушать': ['лампа', 'лампочка', 'люстра']
    }
    for k, v in storage.items():
        result = puzzles(k, v)
        save_results(k, result)
        print('You havn\'t guessed.' if not result else f'You have guessed with {result} attempts!')

def save_results(text: str, num: int):
    _data[text] = num

def show_results():
    res = (
        f'You havn\'t guessed.' if not v
        else f'You have guessed the riddle {k} with {v} attempts!'
        for k, v in _data.items()
    )
    print(*res, sep='\n')

if __name__ == '__main__':
    # puzzles('Зимой и летом одним цветом', ['ель', 'елка', 'ёлка', 'сосна'])
    puzzle_storage()
    show_results()

