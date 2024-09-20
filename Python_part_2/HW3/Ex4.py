# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

backpack = {"matches": 0.5, "sleeping bag": 3.0, "firewood": 5.0, "axe": 1.5, "water": 3.0, "food": 4.5,
            "dishes": 1.0, "tent": 4.5, "flashlight": 0.5, "mat": 1.0, "compass": 0.05, "powerbank": 0.6}

load_capacity = float(input('Enter a maximum weight of the backpack:  '))

dict_items = backpack.items()
final_set = []
list_items = list(dict_items)

for i in range(len(list_items) - 1):
    weight = 0
    backpack_set = []
    weight += list_items[i][1]
    backpack_set.append(list_items[i][0])
    if weight > load_capacity:
        weight -= list_items[i][1]
        backpack_set.pop()
    for j in range(i + 1, len(list_items)):
        weight += list_items[j][1]
        backpack_set.append(list_items[j][0])
        if weight > load_capacity:
            weight -= list_items[j][1]
            backpack_set.pop()
    if  backpack_set == []:
        pass
    elif backpack_set not in final_set:
        final_set.append(backpack_set)

print(f'Possible combinations of items in the backpack within the established weight are: \n{final_set}')
