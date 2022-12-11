"""
Определить максимальные значения для каждого столбца каждой из трех матриц A (4×5), B (5×7), C (3×4)
"""

import numpy as np


# Функция создания матрицы
def creating_matrix(row, col) -> np.ndarray:
    matrix: np.ndarray = np.zeros((row, col))
    for i in range(row):
        for j in range(col):
            matrix[i, j] = float(input('Введите элемент матрицы: '))
    return matrix


# Функция поиска максимального значения в столбце
def maximum_column_value(matrix, row, col):
    max = np.zeros(col)
    for j in range(col):
        max[j] = matrix[0, j]
        for i in range(row):
            if matrix[i, j] > max[j]:
                max[j] = matrix[i, j]
    return max


# Функция вывода результата
def resout(max1):
    print('Максимальные значения для каждого столбца матрицы A: ', max1)
    # print('Максимальные значения для каждого столбца матрицы B: ', max2)
    # print('Максимальные значения для каждого столбца матрицы C: ', max3)


if __name__ == '__main__':
    # Создание матриц
    row = 2
    col = 3
    A = creating_matrix(row, col)
    print(A)
    # n = 5
    # m = 7
    # B = matrix(n, m)
    # n = 3
    # m = 4
    # C = matrix(n, m)

    # Поиск максимальных значений
    max1 = maximum_column_value(A, row, col)
    # max2 = max_col(B, n)
    # max3 = max_col(C, n)

    # Вывод результата
    resout(max1)