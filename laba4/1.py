import numpy as np

eps = 1e-8

def create_system(n, alpha):
    A = 2 * np.eye(n)
    for i in range(n - 1):
        A[i, i+1] = -1 - alpha
        A[i+1, i] = -1 + alpha
    f = np.zeros(n)
    f[0] = 1 - alpha
    f[-1] = 1 + alpha
    return A, f

def jacobi(A, f, max_iter=10000):
    n = len(f)
    x = np.zeros(n)
    iter = max_iter
    D_inv = 0.5 * np.eye(n)
    for it in range(1, max_iter+1):
        x_new = x - D_inv @ (A @ x - f)
        
        if (np.max(np.abs(x_new - x)) < eps):
            iter = it
            x = x_new.copy()
            break
        x = x_new.copy()
    return x, iter

def seidel(A, f, max_iter=10000):
    iter = max_iter
    n = len(f)
    x = np.zeros(n)
    upper = np.triu(A, k=1)
    LD = np.tril(A)
    for it in range(1, max_iter+1):
        rhs = f - upper @ x
        x_new = np.linalg.solve(LD, rhs)
        if (np.max(np.abs(x_new - x)) < eps):
            iter = it
            x = x_new.copy()
            break
        x = x_new.copy()
    return x, iter

n_values = [10, 20, 50]
alpha_values = np.arange(0, 1.01, 0.1)

print(f"n\talpha\titer_jacobi\titer_seidel")
for n in n_values:
    for alpha in alpha_values:
        A, f = create_system(n, alpha)
        x_jacobi, iter_jacobi = jacobi(A, f)
        x_seidel, iter_seidel = seidel(A, f)
        print(f'{n}\t{alpha:.2}\t\t{iter_jacobi}\t\t{iter_seidel}')