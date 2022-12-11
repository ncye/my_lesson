"""
Определить максимальные значения для каждого столбца каждой из трех матриц A (4×5), B (5×7), C (3×4)
"""

import numpy as np


# Функция создания матрицы
def matrix(row, col) -> np.ndarray:
    matrix = np.zeros((row, col))
    for i in range(row):
        for j in range(col):
            A[i, j] = float(input('Введите элемент матрицы: '))
    return matrix


# Функция поиска максимального значения в столбце
def max_col(matrix, n):
    max_col = 0
    for i in range(n):
        if matrix[i, 0] > max_col:
            max_col = matrix[i, 0]
    return max_col


# Функция вывода результата
def resout(max1, max2, max3):
    print('Максимальные значения для каждого столбца матрицы A: ', max1)
    print('Максимальные значения для каждого столбца матрицы B: ', max2)
    print('Максимальные значения для каждого столбца матрицы C: ', max3)


# Создание матриц
n = 4
m = 5
A = matrix(n, m)
n = 5
m = 7
B = matrix(n, m)
n = 3
m = 4
C = matrix(n, m)

# Поиск максимальных значений
max1 = max_col(A, n)
max2 = max_col(B, n)
max3 = max_col(C, n)

# Вывод результата
resout(max1, max2, max3)
