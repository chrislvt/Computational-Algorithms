from one_sided import *
from central import *
from runge import *
from reshape import *
from second_central import *
from prettytable import PrettyTable


xdata = [1, 2, 3, 4, 5, 6]
ydata = [0.571, 0.889, 1.091, 1.231, 1.333, 1.412]

table = [xdata, ydata, [], [], [], [], []]

step = 1

data_12 = RightOneSided(ydata, step)
data_11 = LeftOneSided(ydata, step)
data_2 = Central(ydata, step)
data_32 = RightRunge(ydata, step)
data_31 = LeftRunge(ydata, step)
data_42 = RightReshape(xdata, ydata)
data_41 = LeftReshape(xdata, ydata)
data_5 = SecondCentral(ydata, step)


table = PrettyTable()
table.add_column("x", xdata)
table.add_column("y", ydata)
table.add_column("Левосторонняя", data_11)
table.add_column("Правосторонняя", data_12)
table.add_column("Центральная", data_2)
table.add_column("Рунже, в основе л-я ф-ла", data_31)
table.add_column("Рунже, в основе п-я ф-ла", data_32)
table.add_column("Выравнивающая, в основе л-я ф-ла", data_41)
table.add_column("Выравнивающая, в основе п-я ф-ла", data_42)
table.add_column("Вторая центральная", data_5)


print(table)
