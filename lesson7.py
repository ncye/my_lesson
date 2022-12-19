"""
Определить максимальные значения для каждого столбца каждой из трех матриц A (4×5), B (5×7), C (3×4)
"""

import numpy as np


# Функция создания матрицы с случайными числами
def creating_matrix(row, column):
    matrix = np.random.randint(-100, 100, (row, column), dtype=np.int32)
    return matrix

    # matrix = np.zeros((row, column))
    # for i in range(row):
    #     for j in range(column):
    #         matrix[i, j] = int(input('Введите элемент матрицы: '))
    # return matrix


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
    n = 4
    m = 5
    A = creating_matrix(n, m)
    max1 = maximum_column_value(A, n, m)
    print(A)
    n = 5
    m = 7
    B = creating_matrix(n, m)
    max2 = maximum_column_value(B, n, m)
    print(B)
    n = 3
    m = 4
    C = creating_matrix(n, m)
    max3 = maximum_column_value(C, n, m)
    print(C)

    # Вывод результата
    resout(max1, max2, max3)

