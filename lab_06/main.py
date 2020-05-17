
# Правая разносторонняя производная
def right(y_cur, y_next, h):
    return (y_next - y_cur) / h


# Левая разносторонняя производная
def left(y_cur, y_prev, h):
    return (y_cur - y_prev) / h


# Метод односторонних производных
def method_1(input_data, step):
    output_data = []
    for i in range(len(input_data) - 1):
        output_data.append(right(input_data[i], input_data[i + 1], h))

    output_data.append(left(data[len(input_data) - 1], data[len(input_data) - 2], h))

    return output_data

x = [1, 2, 3, 4, 5, 6]
data = [0.571, 0.889, 1.091, 1.231, 1.333, 1.412]

table = [x, data, [], [], [], [], []]

h = 1

d1 = method_1(data, h)

print(d1)