def second_central(y_cur, y_prev, y_next, step):
    return (y_prev - 2 * y_cur + y_next) / step ** 2


# Вторая производная
def SecondCentral(ydata, step):
    result = ["-"]
    for i in range(1, len(ydata) - 1):
        result.append("{:.3f}".format(second_central(ydata[i], ydata[i - 1], ydata[i + 1], step)))

    result.append("-")

    return result