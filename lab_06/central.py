# Центральная формула для левой производной
def center(y_next, y_prev, step):
    return (y_next - y_prev) / (2 * step)


# Центральная формула для x0
def center_x0(y_0, y_1, y_2, step):
    return (-3 * y_0 + 4 * y_1 - y_2) / (2 * step)


# Так... а это для xn
def center_xn(y_n, yn_1, yn_2, step):
    return (3 * y_n - 4 * yn_1 + yn_2) / (2 * step)


def Central(input_data, step):
    result = [center_x0(input_data[0], input_data[1], input_data[2], step)]

    length = len(input_data)
    for i in range(1, length - 1):
        result.append(center(input_data[i + 1], input_data[i - 1], step))

    result.append(center_xn(input_data[length - 1], input_data[length - 2], input_data[length - 3], step))

    return ["{:.3f}".format(i) for i in result]

