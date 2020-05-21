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

# d2 = method_2(y, h)
# d3_1 = method_3_1(y, h)
# d3_2 = method_3_2(y, h)
# d4 = method_4(x, y)
# d5 = method_5(y, h)
#
#
# print(d1)
# print(d2)
# print(d3_1)
# print(d3_2)
# print(d4)
# print(d5)

table = PrettyTable()
table.add_column("x", xdata)
table.add_column("y", ydata)
table.add_column("Правосторонная", data_11)
table.add_column("Левосторонняя", data_12)
table.add_column("Центральная", data_2)
# #table.add_column("3_1", ['{:.3f}'.format(num) for num in d3_1])
# table.add_column("3_2", ['{:.3f}'.format(num) for num in d3_2])
# table.add_column("5", ['{:.3f}'.format(num) for num in d5])


print(table)
