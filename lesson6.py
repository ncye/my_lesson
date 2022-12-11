"""
Для матрицы A (7×4) вычислить общую сумму элементов строк, первый элемент которых положителен,
а для матрицы B (6×4) — общую сумму элементов строк, в которых первый элемент больше единицы.
Разработайте программу с использованием классов и наследования.
"""


class Matrix:
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.matrix = []
        for i in range(self.m):
            self.matrix.append([])
            for j in range(self.n):
                self.matrix[i].append(0)

    def print_matrix(self):
        for i in range(self.m):
            for j in range(self.n):
                print(self.matrix[i][j], end=' ')
            print()

    def input_matrix(self):
        for i in range(self.m):
            for j in range(self.n):
                self.matrix[i][j] = int(input('Введите элемент матрицы: '))

    def summastr(self, srav):
        sum = 0
        for i in range(self.m):
            if self.matrix[i][0] > srav:
                for j in range(self.n):
                    sum += self.matrix[i][j]
        return sum


class MatrixA(Matrix):
    def __init__(self, m, n):
        super().__init__(m, n)

    def summastr(self):
        return super().summastr(0)


class MatrixB(Matrix):
    def __init__(self, m, n):
        super().__init__(m, n)

    def summastr(self, srav):
        return super().summastr(1)


def resout(sum1, sum2):
    print('Сумма элементов строк матрицы A, первый элемент которых положителен: ', sum1)
    print('Сумма элементов строк матрицы B, первый элемент которых больше единицы: ', sum2)


def main():
    n = 7
    m = 4
    A = MatrixA(n, m)
    A.input_matrix()
    sum1 = A.summastr()
    n = 6
    B = MatrixB(n, m)
    B.input_matrix()
    sum2 = B.summastr()
    resout(sum1, sum2)


main()
