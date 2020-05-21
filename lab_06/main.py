from one_sided_derivative import *
from central_derivative import *
from runge import *
from reshape import *
from second_central import *
from prettytable import PrettyTable


x = [1, 2, 3, 4, 5, 6]
y = [0.571, 0.889, 1.091, 1.231, 1.333, 1.412]

table = [x, y, [], [], [], [], []]

h = 1

d1 = method_1(y, h)
d2 = method_2(y, h)
d3_1 = method_3_1(y, h)
d3_2 = method_3_2(y, h)
d4 = method_4(x, y)
d5 = method_5(y, h)


print(d1)
print(d2)
print(d3_1)
print(d3_2)
print(d4)
print(d5)

# table = PrettyTable()
# table.add_column("x", x)
# table.add_column("y", y)
# table.add_column("1", ['{:.3f}'.format(num) for num in d1])
# #table.add_column("2", ['{:.3f}'.format(num) for num in d2])
# #table.add_column("3_1", ['{:.3f}'.format(num) for num in d3_1])
# table.add_column("3_2", ['{:.3f}'.format(num) for num in d3_2])
# table.add_column("5", ['{:.3f}'.format(num) for num in d5])





# print(table)
