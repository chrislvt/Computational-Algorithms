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

data_11 = RightOneSided(ydata, step)
data_12 = LeftOneSided(ydata, step)
data_2 = Central(ydata, step)
data_31 = RightRunge(ydata, step)
data_32 = LeftRunge(ydata, step)
data_41 = RightReshape(xdata, ydata)
data_42 = LeftReshape(xdata, ydata)



table = PrettyTable()
table.add_column("x", xdata)
table.add_column("y", ydata)
table.add_column("Правосторонная", data_11)
table.add_column("Левосторонняя", data_12)
table.add_column("Центральная", data_2)
table.add_column("Рунже правая", data_31)
table.add_column("Рунже левая", data_32)
table.add_column("Выравнивающая правая", data_41)
table.add_column("Выравнивающая левая", data_42)

# table.add_column("5", ['{:.3f}'.format(num) for num in d5])


print(table)
