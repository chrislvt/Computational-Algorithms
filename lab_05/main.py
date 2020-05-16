import matplotlib.pyplot as plt
from prettytable import PrettyTable
from integral_solution import *

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

        plt.plot(xdata, ydata)
        plt.grid(True)
        plt.show()

    elif choice == 2:
        print("Не забудьте приблизить график! ;)")

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
        print("Не забудьте приблизить график! ;)")

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
