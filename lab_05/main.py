from math import *
from gauss_method import *
import matplotlib.pyplot as plt
from prettytable import PrettyTable


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
def NewtonMethod(i, n):
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
        nodes.append(NewtonMethod(i, n))

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


# Метод Симпсона.
def Magic(N, M, tau):
    a = 0
    b = pi / 2

    # Господь всемогущий... это же для вычисления phi!
    step = (b - a) / (N - (N % 2))

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


# Вывод графика на экран
def make_plot(xdata, ydata):
    plt.plot(xdata, ydata)
    plt.grid(True)
    plt.show()


print("Главное меню:")
print("1 - Самостоятельно задать n и m.")
print("2 - Вывести изменение по Симпсону.")
print("3 - Вывести изменение по Гауссу.")
print("4 - Таблица для tau.")
print("0 - Выход.")


t = True
while t:
    choice = int(input("Выберите действие: "))

    if choice == 1:
        n = int(input("Введите кол-во участков разбиения по Симпсону: "))
        m = int(input("Введите кол-во участков разбиения по Гауссу: "))

        tau = 0.005
        xdata, ydata = [], []
        while tau < 10:
            result = Result(n, m, tau)
            xdata.append(tau)
            ydata.append(result)
            tau += 0.1

        for i in range(len(ydata)):
            print(ydata[i])

        make_plot(xdata, ydata)

    elif choice == 2:
        for i in range(3, 10, 2):
            x, y = [], []
            tau = 0.005
            while tau < 10:
                result = Result(i, 10, tau)
                x.append(tau)
                y.append(result)
                tau += 0.1

            lb = "N = " + str(i) + ", M =" + str(10)
            plt.plot(x, y, label=lb)
            plt.legend()
            plt.grid(True)

        plt.show()

    elif choice == 3:
        for i in range(3, 10, 2):
            x, y = [], []
            tau = 0.005
            while tau < 10:
                result = Result(10, i, tau)
                x.append(tau)
                y.append(result)
                tau += 0.1

            lb = "N = " + str(10) + ", M =" + str(i)
            plt.plot(x, y, label=lb)
            plt.legend()
            plt.grid(True)

        plt.show()

    elif choice == 4:
        y1, y2 = [], []
        for i in range(3, 15):
            result1 = Result(i, 10, 1)
            result2 = Result(10, i, 1)
            y1.append(result1)
            y2.append(result2)

        table = PrettyTable()
        table.add_column("Кол-во узлов", [i for i in range(3, 15)])
        table.add_column("Изменение по Симпсону", y1)
        table.add_column("Изменение по Гауссу", y2)

        print(table)

    elif choice == 0:
        t = False