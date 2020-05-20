def second_central(y_cur, y_prev, y_next, step):
    return (y_prev - 2 * y_cur + y_next) / step ** 2


# Вторая производная
def method_5(input_data, step):
    output_data = []
    for i in range(1, len(input_data) - 1):
        output_data.append(second_central(input_data[i], input_data[i - 1], input_data[i + 1], step))

    return output_data