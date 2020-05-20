#  Ну тут очевидно по названию что эта формула делает
def Runge_right(y_cur, y_next, y_next_next, step):
    return (4 * y_next - 3 * y_cur - y_next_next) / (2 * step)


def Runge_left(y_cur, y_prev, y_prev_prev, step):
    return (3 * y_cur - 4 * y_prev + y_prev_prev) / (2 * step)

# Формула Рунге с правосторонней производной
def method_3_1(input_data, step):
    output_data = []
    for i in range(len(input_data) - 2):
        output_data.append(Runge_right(input_data[i], input_data[i + 1], input_data[i + 2], step))

    return output_data


# Формула Рунге с левосторонней производной
def method_3_2(input_data, step):
    output_data = []
    for i in range(2, len(input_data)):
        output_data.append(Runge_left(input_data[i], input_data[i - 1], input_data[i - 2], step))

    return output_data
