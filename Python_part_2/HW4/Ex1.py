# Напишите функцию для транспонирования матрицы

def matrix_transposition(data: list[list]) -> list[list]:
    transposed_matrix = [[data[j][i] for j in range(len(data))] for i in range(len(data[0]))]
    return transposed_matrix

matrix = [[1, 2, 3], [4, 5, 6]]
print(matrix_transposition(matrix))
