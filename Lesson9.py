"""
Определить максимальные значения для каждого столбца каждой из трех матриц A (4×5), B (5×7), C (3×4)
Использовать GUI
"""
import numpy as np
from tkinter import *
from tkinter import messagebox


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
class Resout(MaximumColumnValue):
    def __init__(self, row, column):
        super().__init__(row, column)

    def resout(self, maximum_column_value_1, maximum_column_value_2, maximum_column_value_3):
        messagebox.showinfo('Результат', f'Максимальные значения для каждого столбца матрицы A: {maximum_column_value_1}\n'
                                         f'Максимальные значения для каждого столбца матрицы B: {maximum_column_value_2}\n'
                                         f'Максимальные значения для каждого столбца матрицы C: {maximum_column_value_3}')


# Класс создания GUI
class GUI:
    def __init__(self):
        self.root = Tk()
        self.root.title('Максимальные значения для каждого столбца каждой из трех матриц')
        self.root.geometry('500x300')
        self.root.resizable(False, False)
        self.root['bg'] = 'lightblue'
        self.label = Label(self.root, text='Введите количество строк и столбцов для матриц A, B, C', bg='lightblue')
        self.label.grid(row=0, column=0, columnspan=2, pady=10)
        self.label_row = Label(self.root, text='Количество строк: ', bg='lightblue')
        self.label_row.grid(row=1, column=0, pady=10)
        self.label_column = Label(self.root, text='Количество столбцов: ', bg='lightblue')
        self.label_column.grid(row=2, column=0, pady=10)
        self.entry_row = Entry(self.root)
        self.entry_row.grid(row=1, column=1, pady=10)
        self.entry_column = Entry(self.root)
        self.entry_column.grid(row=2, column=1, pady=10)
        self.button = Button(self.root, text='Рассчитать', command=self.button_click)
        self.button.grid(row=3, column=0, columnspan=2, pady=10)
        self.root.mainloop()

    def button_click(self):
        try:
            row = int(self.entry_row.get())
            column = int(self.entry_column.get())
            if row <= 0 or column <= 0:
                messagebox.showerror('Ошибка', 'Количество строк и столбцов должно быть больше нуля')
            else:
                creating_matrix_1 = CreatingMatrix(row, column)
                creating_matrix_2 = CreatingMatrix(row + 1, column + 2)
                creating_matrix_3 = CreatingMatrix(row - 1, column - 2)
                matrix_1 = creating_matrix_1.creating_matrix()
                matrix_2 = creating_matrix_2.creating_matrix()
                matrix_3 = creating_matrix_3.creating_matrix()
                maximum_column_value_1 = MaximumColumnValue(row, column)
                maximum_column_value_2 = MaximumColumnValue(row + 1, column + 2)
                maximum_column_value_3 = MaximumColumnValue(row - 1, column - 2)
                maximum_column_value_1 = maximum_column_value_1.maximum_column_value(matrix_1)
                maximum_column_value_2 = maximum_column_value_2.maximum_column_value(matrix_2)
                maximum_column_value_3 = maximum_column_value_3.maximum_column_value(matrix_3)
                resout = Resout(row, column)
                resout.resout(maximum_column_value_1, maximum_column_value_2, maximum_column_value_3)
        except ValueError:
            messagebox.showerror('Ошибка', 'Количество строк и столбцов должно быть целым числом')


if __name__ == '__main__':
    gui = GUI()



