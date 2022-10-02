from scipy.optimize import minimize
import numpy as np
import numpy


def makeData():
    x = numpy.linspace(-10, 10, 100)
    y = numpy.linspace(-10, 10, 100)

    xgrid, ygrid = numpy.meshgrid(x, y)

    z = 2 * xgrid * xgrid + 2 * xgrid * ygrid + 2 * ygrid * ygrid - 4 * xgrid - 6 * ygrid
    return xgrid, ygrid, z


def kp():
    global points
    points = []

    def fun(x):  # Конкретная функция, которую просила Полупанова
        x1 = x[0]
        x2 = x[1]
        return 2 * x1 * x1 + 2 * x1 * x2 + 2 * x2 * x2 - 4 * x1 - 6 * x2

    def constraint(x):  # констрейнт, необходимый для работы
        x1 = x[0]
        x2 = x[1]
        return x1 + 2 * x2 - 2

    def callback(Xi):
        global points
        glist = np.ndarray.tolist(Xi)
        glist.append(fun(Xi))
        points.append(glist)

    b = (0, float("inf"))  # диапозон поиска
    bnds = (b, b)
    x0 = (4, 2)  # начальная точка
    con = {'type': 'eq', 'fun': fun}

    # основной вызов
    res = minimize(fun, x0, method="SLSQP", bounds=bnds,
                   constraints=con, callback=callback)

    glist = np.ndarray.tolist(res.x)
    glist.append(res.fun)
    points.append(glist)

    for iteration, point in enumerate(points):
        yield iteration, point
