import numpy as np

def polinomio_de_lagrange(x, xn, yn):
    y = 0
    for i in range(len(xn)):
        lagrange = yn[i]
        for j in range(len(xn)):
            if i != j:
                lagrange *= (x - xn[j]) / (xn[i] - xn[j])
        y += lagrange
    return y


def diferencias_divididas(x, xn, yn):
    y = 0
    n = len(xn)
    m = np.zeros([n, n+1])
    for i in range(n):
        m[i][0] = xn[i]
        m[i][1] = yn[i]
    for i in range(1, n):
        for j in range(2, i+2):
            m[i][j] = (m[i][j-1] - m[i-1][j-1]) / (m[i][0] - m[i-j+1][0])
    for i in range(0, n):
        ax = m[i][i+1]
        for j in range(0, i):
            if i != 0:
                ax *= x - m[j][0]
        y += ax
    return m, y