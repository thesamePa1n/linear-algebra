import numpy as np


def progonka(a, b, c, d):
    n = len(b)

    alpha = np.zeros(n)
    beta = np.zeros(n)

    alpha[0] = -c[0] / b[0]
    beta[0] = d[0] / b[0]

    for i in range(1, n):
        denominator = b[i] + a[i] * alpha[i - 1]

        alpha[i] = -c[i] / denominator

        beta[i] = (d[i] - a[i] * beta[i - 1]) / denominator

    x = np.zeros(n)

    x[n - 1] = beta[n - 1]

    for i in range(n - 2, -1, -1):
        x[i] = alpha[i] * x[i + 1] + beta[i]

    return x

n = 6
a_v = np.array([0, -1, -1, -1, -1, -1], dtype=float)
b_v = np.array([2, 2, 2, 2, 2, 2], dtype=float)
c_v = np.array([-1, -1, -1, -1, -1, 0], dtype=float)
d_v = np.array([3, -4, 4, -4, 4, -3], dtype=float)
x_v = progonka(a_v, b_v, c_v, d_v)

print("Система в)")
print(x_v)

a_g = np.array([0, 1, 1, 2, 1, 2], dtype=float)
b_g = np.array([10, -10, -10, -10, -10, -10], dtype=float)
c_g = np.array([-1, 3, -2, -1, 1, 0], dtype=float)
d_g = np.array([10, 4, -10, 1, -10, 2], dtype=float)
x_g = progonka(a_g, b_g, c_g, d_g)

print("Система г)")
print(x_g)