
# Правая разносторонняя производная
def right(y_cur, y_next, h):
    return (y_next - y_cur) / h


# Левая разносторонняя производная
def left(y_cur, y_prev, h):
    return (y_cur - y_prev) / h


x = [1, 2, 3, 4, 5, 6]
data = [0.571, 0.889, 1.091, 1.231, 1.333, 1.412]

table = [x, data, [], [], [], [], []]

h = 1

d1 = []

# Вычисление производных методом односторонних производных.
for i in range(len(data) - 1):
    d1.append(right(data[i], data[i + 1], h))

d1.append(left(data[len(data) - 1], data[len(data) - 2], h))

print(d1)