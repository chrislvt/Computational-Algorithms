# Правая разносторонняя производная
def right(y_cur, y_next, h):
    return (y_next - y_cur) / h


# Левая разносторонняя производная
def left(y_cur, y_prev, h):
    return (y_cur - y_prev) / h


# Односторонняя разносторонняя производная
def method_1(input_data, step):
    output_data = []
    for i in range(len(input_data) - 1):
        output_data.append(right(input_data[i], input_data[i + 1], step))

    output_data.append(left(input_data[len(input_data) - 1], input_data[len(input_data) - 2], step))

    return output_data
