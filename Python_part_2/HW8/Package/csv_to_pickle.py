# Ex7

__all__ = ['csv_to_pickles']


import csv
from pathlib import Path
import pickle
import json

def csv_to_pickles(path: Path) -> None:
    with open(path, 'r', encoding='UTF-8', newline='') as f_read:
        csv_read = csv.reader(f_read, dialect='excel')
        result = []
        for i, row in enumerate(f_read):
            if i != 0:
                result.append(dict(zip(headers, row)))
            else:
                headers = row

    print(pickle.dumps(result))


if __name__ == '__main__':
    csv_to_pickles(Path('new_users.csv'))