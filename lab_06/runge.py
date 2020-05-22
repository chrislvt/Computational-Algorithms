# Вторая формула Рунге, в основе лежит правосторонняя формула
def runge_right(y_cur, y_next, y_next_next, step):
    return (4 * y_next - 3 * y_cur - y_next_next) / (2 * step)


# Вторая формула Рунге, в основе лежит левосторонняя формула
def runge_left(y_cur, y_prev, y_prev_prev, step):
    return (3 * y_cur - 4 * y_prev + y_prev_prev) / (2 * step)


def RightRunge(ydata, step):
    result = []
    for i in range(len(ydata) - 2):
        result.append("{:.3f}".format(runge_right(ydata[i], ydata[i + 1], ydata[i + 2], step)))

    result.append("-")
    result.append("-")

    return result


def LeftRunge(ydata, step):
    result = ["-", "-"]
    for i in range(2, len(ydata)):
        result.append("{:.3f}".format(runge_left(ydata[i], ydata[i - 1], ydata[i - 2], step)))

    return result