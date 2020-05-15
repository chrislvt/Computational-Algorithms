from math import *
from gauss_method import *
import matplotlib.pyplot as plt


# Подынтегральная формула
def f(tau, phi, teta):
    lR = (2 * cos(teta)) / (1 - (sin(teta) ** 2) * (cos(phi) ** 2))
    return (1 - exp(-1 * tau * lR)) * cos(teta) * sin(teta)


# Полином Лежандра (рекурсивный способ нахождения)
def P(x, n):
    p = [1, x]
    for i in range(2, n + 1):
        p.append(((2 * i - 1) * x * p[i - 1] - (i - 1) * p[i - 2]) / i)

    return p[n]


# Производная полинома Лежандра
def dP(x, n,):
    return (n / (1 - x ** 2)) * (P(x, n - 1) - x * P(x, n))


# Поиск корней полинома Лежандра методом Ньютона.
def NewtonMethod(a, b, i, n):
    xn = cos(pi * ((4 * i - 1) / (4 * n + 2)))
    xn1 = xn - P(xn, n) / dP(xn, n)
    while abs(xn1 - xn) > 1e-10:
        xn = xn1
        xn1 = xn - P(xn, n) / dP(xn, n)

    return xn1


# Поиск узлов t
def FindNodes(n):
    nodes = []
    for i in range(1, n + 1):
        nodes.append(NewtonMethod(-1, 1, i, n))

    return nodes


# Поиск коэффициентов A
def FindCoefficients(nodes):
    matrix = []
    for i in range(len(nodes)):
        matrix.append([])
        for j in range(len(nodes)):
            matrix[i].append(nodes[j] ** i)
        matrix[i].append((1 - (-1) ** (i + 1)) / (i + 1))

    return gaussMethod(matrix)


# Квадратурная формула Гаусса
def GaussQuadrature(tau, phi, m):
    t = FindNodes(m)
    a = FindCoefficients(t)

    c = 0
    d = pi / 2

    sum = 0
    for i in range(m):
        teta = ((d + c) / 2) + ((d - c) / 2) * t[i]
        sum += a[i] * f(tau, phi, teta)

    sum = sum * (d - c) / 2

    return sum


# Последовательное интегрирование.
def Magic(N, M, tau):
    a = 0
    b = pi / 2

    # Господь всемогущий... это же для вычисления phi!
    step = (b - a) / N

    sum = 0
    for i in range(N // 2):
        phi = a + 2 * i * step
        sum += GaussQuadrature(tau, phi, M)

        phi = a + (2 * i + 1) * step
        sum += 4 * GaussQuadrature(tau, phi, M)

        phi = a + (2 * i + 2) * step
        sum += GaussQuadrature(tau, phi, M)

    sum = sum * (step / 3)

    return sum


# Это был долгий путь...
def Result(N, M, tau):
    I = Magic(N, M, tau)
    I = (4 / pi) * I

    return I


def make_plot(xdata, ydata):
    plt.plot(xdata, ydata)
    plt.grid(True)
    plt.show()

# n, m = map(int, input("Введите кол-во участков разбиения по phi и по teta: ").split())
# tau = float(input("Введите tau: "))

n = m = 10
tau = 0.005
x, y = [], []
while tau < 10:
    result = Result(n, m, tau)
    x.append(tau)
    y.append(result)
    tau += 0.1

make_plot(x, y)