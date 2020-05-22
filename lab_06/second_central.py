def second_central(y_cur, y_prev, y_next, step):
    return (y_prev - 2 * y_cur + y_next) / step ** 2


def second_central_x0(y0, y1, y2, y3, step):
    return (4 * y2 - 5 * y1 - y3 + 2 * y0) / step ** 2


def second_central_xn(yn, yn_1, yn_2, yn_3, step):
    return (4 * yn_2 - 5 * yn_1 - yn_3 + 2 * yn) / step ** 2


def SecondCentral(ydata, step):
    result = ["{:.3f}".format(second_central_x0(ydata[0], ydata[1], ydata[2], ydata[3], step))]
    for i in range(1, len(ydata) - 1):
        result.append("{:.3f}".format(second_central(ydata[i], ydata[i - 1], ydata[i + 1], step)))

    n = len(ydata) - 1
    result.append("{:.3f}".format(second_central_xn(ydata[n], ydata[n - 1], ydata[n - 2], ydata[n - 3], step)))

    return result