import numpy as np

eps = 1e-8

def create_system(n):
    A = 2 * np.eye(n)
    for i in range(n - 1):
        A[i, i+1] = -1
        A[i+1, i] = -1
    f = np.zeros(n)
    f[0] = 1
    f[-1] = -1
    return A, f

def SOR(A, f, omega, max_iter=10000):
    n = len(f)
    x = np.zeros(n)
    iter = max_iter
    for it in range(1, max_iter+1):
        x_old = x.copy()
        for i in range(n):
            sum1 = np.dot(A[i, :i], x[:i])
            sum2 = np.dot(A[i, i+1:], x[i+1:])
            x[i] = (1 - omega) * x[i] + (omega / A[i, i]) * (f[i] - sum1 - sum2)
        if (np.max(np.abs(x - x_old)) < eps):
            iter = it
            break
    return x, iter

n_values = [10, 20, 50]
omega_values = np.arange(1.01, 2.0, 0.1)

print(f"n\tomega\titer")
for n in n_values:
    for omega in omega_values:
        A, f = create_system(n)
        x, iter = SOR(A, f, omega)
        print(f'{n}\t{omega:.2}\t\t{iter}')