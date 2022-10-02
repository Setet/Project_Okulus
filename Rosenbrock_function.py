import numpy as np
import numpy


def rosen(x):
    return np.sum(100.0 * (x[1:] - x[:-1] ** 2.0) ** 2.0 + (1 - x[:-1]) ** 2.0, axis=0)


def makeData():
    x = numpy.linspace(-2, 2, 100)
    y = numpy.linspace(-1, 3, 100)

    xgrid, ygrid = numpy.meshgrid(x, y)

    z = rosen(np.array([xgrid, ygrid]))
    return xgrid, ygrid, z
