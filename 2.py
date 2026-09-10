import numpy as np

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
  
n_values = [3, 5, 10, 20]

for n in n_values:
    matrix = np.fromfunction(lambda i, j: np.minimum(i + 1, j + 1), (n, n), dtype=float)
    print(matrix)
    print()
    inv_matrix = np.linalg.inv(matrix)

    cond_A1 = norma_A1(matrix) * norma_A1(inv_matrix)
    cond_AE = norma_AE(matrix) * norma_AE(inv_matrix)
    cond_Ainf = norma_Ainf(matrix) * norma_Ainf(inv_matrix)

    print(f"Размерность n = {n}")
    print(f"cond_A1:   ручной = {cond_A1:.2f} | готовый = {np.linalg.cond(matrix, p=1):.2f}")
    print(f"cond_AE:   ручной = {cond_AE:.2f} | готовый = {np.linalg.cond(matrix, p='fro'):.2f}")
    print(f"cond_Ainf: ручной = {cond_Ainf:.2f} | готовый = {np.linalg.cond(matrix, p=np.inf):.2f}")
    print()