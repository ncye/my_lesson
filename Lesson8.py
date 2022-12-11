"""
Определить максимальные значения для каждого столбца каждой из трех матриц A (4×5), B (5×7), C (3×4)
Использовать классы и наследование
"""
import numpy as np


# Класс создания матрицы с случайными числами
class CreatingMatrix:
    def __init__(self, row, column):
        self.row = row
        self.column = column

    def creating_matrix(self):
        matrix = np.random.randint(-100, 100, (self.row, self.column), dtype=np.int32)
        return matrix


# Класс поиска максимального значения в столбце
class MaximumColumnValue:
    def __init__(self, matrix, row, column):
        self.matrix = matrix
        self.row = row
        self.column = column

    def maximum_column_value(self):
        matrix_max = np.zeros(self.column)
        for j in range(self.column):
            matrix_max[j] = self.matrix[0, j]
            for i in range(self.row):
                if self.matrix[i, j] > matrix_max[j]:
                    matrix_max[j] = self.matrix[i, j]
        return matrix_max


# Класс вывода матрицы
class PrintMatrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def print_matrix(self):
        print(self.matrix)


# Класс вывода максимальных значений столбцов
class PrintMaximumColumnValue:
    def __init__(self, matrix_max):
        self.matrix_max = matrix_max

    def print_maximum_column_value(self):
        print(self.matrix_max)


# Класс вывода максимальных значений столбцов для каждой матрицы
class PrintMaximumColumnValueMatrix:
    def __init__(self, matrix_max):
        self.matrix_max = matrix_max

    def print_maximum_column_value_matrix(self):
        print('Максимальные значения столбцов матрицы A: ', self.matrix_max[0])
        print('Максимальные значения столбцов матрицы B: ', self.matrix_max[1])
        print('Максимальные значения столбцов матрицы C: ', self.matrix_max[2])


if __name__ == '__main__':
    matrix_max = []
    matrix = CreatingMatrix(4, 5)
    matrix_max.append(MaximumColumnValue(matrix.creating_matrix(), 4, 5).maximum_column_value())
    matrix = CreatingMatrix(5, 7)
    matrix_max.append(MaximumColumnValue(matrix.creating_matrix(), 5, 7).maximum_column_value())
    matrix = CreatingMatrix(3, 4)
    matrix_max.append(MaximumColumnValue(matrix.creating_matrix(), 3, 4).maximum_column_value())
    PrintMaximumColumnValueMatrix(matrix_max).print_maximum_column_value_matrix()
