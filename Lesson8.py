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


# Класс вывода результата
def resout(maximum_column_value_1, maximum_column_value_2, maximum_column_value_3):
    print('Максимальные значения для каждого столбца матрицы A: ', maximum_column_value_1)
    print('Максимальные значения для каждого столбца матрицы B: ', maximum_column_value_2)
    print('Максимальные значения для каждого столбца матрицы C: ', maximum_column_value_3)


if __name__ == '__main__':
    matrix_A = CreatingMatrix(4, 5).creating_matrix()
    maximum_column_value_A = MaximumColumnValue(4, 5).maximum_column_value(matrix_A)

    matrix_B = CreatingMatrix(5, 7).creating_matrix()
    maximum_column_value_B = MaximumColumnValue(5, 7).maximum_column_value(matrix_B)

    matrix_C = CreatingMatrix(3, 4).creating_matrix()
    maximum_column_value_C = MaximumColumnValue(3, 4).maximum_column_value(matrix_C)

    resout(maximum_column_value_A, maximum_column_value_B, maximum_column_value_C)
