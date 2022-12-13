"""
Определить максимальные значения для каждого столбца каждой из трех матриц A (4×5), B (5×7), C (3×4)
Использовать GUI
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
class MaximumColumnValue(CreatingMatrix):
    def __init__(self, row, column):
        super().__init__(row, column)

    def maximum_column_value(self, matrix):
        matrix_max = np.zeros(self.column)
        for j in range(self.column):
            matrix_max[j] = matrix[0, j]
            for i in range(self.row):
                if matrix[i, j] > matrix_max[j]:
                    matrix_max[j] = matrix[i, j]
        return matrix_max


