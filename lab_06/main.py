from one_sided_derivative import *
from central_derivative import *
from runge import *
from reshape import *
from second_central import *


x = [1, 2, 3, 4, 5, 6]
data = [0.571, 0.889, 1.091, 1.231, 1.333, 1.412]

table = [x, data, [], [], [], [], []]

h = 1

d1 = method_1(data, h)
d2 = method_2(data, h)
d3_1 = method_3_1(data, h)
d3_2 = method_3_2(data, h)

d5 = method_5(data, h)


print(d1)
print(d2)
print(d3_1)
print(d3_2)

print(d5)
