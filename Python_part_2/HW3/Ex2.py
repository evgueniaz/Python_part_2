# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.


original_list = [3, 45, 78, 3, 1, 976, 3, 78, 5, 2, 1, 45, 1, 74, 1, 234, 67, 54, 976]
original_set = set(original_list)
doubles_list = []
for item in original_set:
    if original_list.count(item) > 1:
        doubles_list.append(item)

print(f'The list of repeated elements is {doubles_list}')