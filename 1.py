import numpy as np
import scipy.linalg as linalg

def norma_x1(vector):
    return sum(np.abs(vector))

def norma_x2(vector):
    return sum(np.abs(vector) ** 2) ** (1 / 2)

def norma_inf(vector):
    return max(np.abs(vector))

n = int(input("Введите n: "))
print()
vector = np.random.randint(-10, 11, size=n)
print(vector)
print()
print('Норма вектора x1:', norma_x1(vector))
print('Готовая норма вектора x1:', linalg.norm(vector, ord=1))
print()
print('Норма вектора x2:', norma_x2(vector))
print('Готовая норма вектора x2:', linalg.norm(vector))
print()
print('Норма вектора x_inf:', norma_inf(vector))
print('Готовая норма вектора x_inf:', linalg.norm(vector, ord=np.inf))
print()

matrix = np.random.randint(-10, 11, size=(n, n))
print(matrix)
print()

def norma_A1(mat):
    maximum = mat[0][0]
    for i in range(len(mat)):
        summa = 0
        for j in range(len(mat)):
            summa += abs(mat[j][i])
        if (summa > maximum):
            maximum = summa
    return maximum

def norma_AE(mat):
    summa = 0
    for i in range(len(mat)):
        for j in range(len(mat)):
            summa += abs(mat[i][j]) ** 2
    return summa ** (1/2)

def norma_Ainf(mat):
    maximum = mat[0][0]
    for i in range(len(mat)):
        summa = 0
        for j in range(len(mat)):
            summa += abs(mat[i][j])
        if (summa > maximum):
            maximum = summa
    return maximum

norm_A1 = norma_A1(matrix)
norm_AE = norma_AE(matrix)
norm_Ainf = norma_Ainf(matrix)

print('Норма матрицы A1:', norm_A1)
print('Готовая норма матрицы A1:', linalg.norm(matrix, ord=1))
print()
print('Норма матрицы AE:', norm_AE)
print('Готовая норма матрицы AE:', linalg.norm(matrix))
print()
print('Норма матрицы Ainf:', norm_Ainf)
print('Готовая норма матрицы Ainf:', linalg.norm(matrix, ord=np.inf))
print()

if (1 / np.sqrt(n)) * norm_A1 <= norm_AE <= np.sqrt(n) * norm_A1:
    print('Неравенство выполнено при alpha = 1')
if (1 / np.sqrt(n)) * norm_Ainf <= norm_AE <= np.sqrt(n) * norm_Ainf:
    print('Неравенство выполнено при alpha = inf')