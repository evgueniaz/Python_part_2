# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где
# ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем,
# используйте его строковое представление.


def pass_to_dict(**kwargs) -> dict:
    result = {}
    for key, value in kwargs.items():
        try:
            result[value] = key
        except:
            result[str(value)] = key
    return result

print(pass_to_dict(store='K-Mart', city='San Antonio', age=45,
                     varieties=['Sultana', 'Tompson', 'Mercedes'],
                     food={'fruit': 'grapes', 'vegitable': 'cucumber', 'beverage': 'juice'}))

