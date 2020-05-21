# ща как заработает

def eta(y):
    return 1 / y


def ksi(x):
    return 1 / x


def reshape(y_cur, y_next, x_cur, x_next):
    return (eta(y_next) - eta(y_cur)) / (ksi(x_next) - ksi(x_cur)) * (y_cur / x_cur) ** 2


# Производная, полученная с помощью метода выравниающих переменных
def method_4(xdata, ydata):
    output_data = []
    for i in range(len(ydata) - 1):
        output_data.append(reshape(ydata[i], ydata[i + 1], xdata[i], xdata[i + 1]))

    return output_data