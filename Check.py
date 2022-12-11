"""
Даны матрицы A (5×5), B (7×7), C (4×4). Вычислить значение выражения PA + PB – PC, где PA (PB, PC) — произведение
положительных элементов главной диагонали матрицы (A B, C)
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


