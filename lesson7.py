"""
Определить максимальные значения для каждого столбца каждой из трех матриц A (4×5), B (5×7), C (3×4)
"""

import numpy as np


# Функция создания матрицы
def creating_matrix(row, column) -> np.ndarray:
    matrix: np.ndarray = np.zeros((row, column))
    for i in range(row):
        for j in range(column):
            matrix[i, j] = float(input('Введите элемент матрицы: '))
    return matrix


# Функция поиска максимального значения в столбце
def maximum_column_value(matrix, row, column):
    matrix_max = np.zeros(column)
    for j in range(column):
        matrix_max[j] = matrix[0, j]
        for i in range(row):
            if matrix[i, j] > matrix_max[j]:
                matrix_max[j] = matrix[i, j]
    return matrix_max


# Функция вывода результата
def resout(maximum_column_value_1, maximum_column_value_2, maximum_column_value_3):
    print('Максимальные значения для каждого столбца матрицы A: ', maximum_column_value_1)
    print('Максимальные значения для каждого столбца матрицы B: ', maximum_column_value_2)
    print('Максимальные значения для каждого столбца матрицы C: ', maximum_column_value_3)


if __name__ == '__main__':
    # Создание матриц
    n = 2
    m = 3
    A = creating_matrix(n, m)
    print(A)
    n = 5
    m = 7
    B = creating_matrix(n, m)
    n = 3
    m = 4
    C = creating_matrix(n, m)

    # Поиск максимальных значений
    max1 = maximum_column_value(A, n, m)
    max2 = maximum_column_value(B, n, m)
    max3 = maximum_column_value(C, n, m)

    # Вывод результата
    resout(max1, max2, max3)
