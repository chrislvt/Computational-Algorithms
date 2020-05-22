def eta(y):
    return 1 / y


def ksi(x):
    return 1 / x


# В основе лежит правосторонняя формула
def right_reshape(y_cur, y_next, x_cur, x_next):
    return (eta(y_next) - eta(y_cur)) / (ksi(x_next) - ksi(x_cur)) * (y_cur / x_cur) ** 2


# В основе лежит левосторонняя формула.
def left_reshape(y_cur, y_prev, x_cur, x_prev):
    return (eta(y_cur) - eta(y_prev)) / (ksi(x_cur) - ksi(x_prev)) * (y_cur / x_cur) ** 2


def RightReshape(xdata, ydata):
    result = []
    for i in range(len(ydata) - 1):
        result.append("{:.3f}".format(right_reshape(ydata[i], ydata[i + 1], xdata[i], xdata[i + 1])))

    result.append("-")

    return result


def LeftReshape(xdata, ydata):
    result = ["-"]
    for i in range(1, len(ydata)):
        result.append("{:.3f}".format(left_reshape(ydata[i], ydata[i - 1], xdata[i], xdata[i - 1])))

    return result