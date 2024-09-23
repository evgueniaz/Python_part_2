# Создайте функцию генератор чисел Фибоначчи

def fibonacci_nums(limit: int):
    series = [1, 1]
    for i in range(limit - 2):
        series.append(series[i] + series[i + 1])
    return series[: limit]

limit = int(input('Enter a whole number for the quantity of Fibonacci numbers too be shown:  '))
print(f'The first {limit} Fibonacci numbers are: {fibonacci_nums(limit)}')