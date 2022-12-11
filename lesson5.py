# Для матрицы А (7х4) вычислить общую сумму элементов строк,
# первый элемент которых положителен
# Для матрицы В (6х4) общую сумму элементов строк, в которых элемент больше единицы
import numpy as np


def matrin(n, m):
    A = np.zeros((n, m))
    for i in range(n):
        for j in range(m):
            A[i, j] = float(input('Введите элемент матрицы: '))
    return A


def summastr(A, n, m, srav):
    sum = 0
    for i in range(n):
        if A[i, 0] > srav:
            for j in range(m):
                sum += A[i, j]
    return sum


def resout(sum1, sum2):
    print('Сумма элементов строк матрицы A, первый элемент которых положителен: ', sum1)
    print('Сумма элементов строк матрицы B, первый элемент которых больше единицы: ', sum2)


n = 7
m = 4
A = matrin(n, m)
sum1 = summastr(A, n, m, 0)
n = 6
B = matrin(n, m)
sum2 = summastr(B, n, m, 1)
resout(sum1, sum2)
