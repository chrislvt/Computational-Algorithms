# Правая разносторонняя производная
def right(y_cur, y_next, step):
    return (y_next - y_cur) / step


# Левая разносторонняя производная
def left(y_cur, y_prev, step):
    return (y_cur - y_prev) / step


# Вычисление производных с помощью правосторонней формулы
def RightOneSided(ydata, step):
    result = []
    for i in range(len(ydata) - 1):
        result.append("{:.3f}".format(right(ydata[i], ydata[i + 1], step)))

    result.append("-")

    return result


# Вычисление производных с помощью левосторонней формулы
def LeftOneSided(ydata, step):
    result = ["-"]
    for i in range(1, len(ydata)):
        result.append("{:.3f}".format(left(ydata[i], ydata[i - 1], step)))

    return result
