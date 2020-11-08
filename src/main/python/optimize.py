import numpy as np
from xfoil import XFoil
import airfoils

nacaSet = [6, 7, 9, 10, 12, 15, 18, 21, 24, 1408, 1410, 1412, 2408, 2410, 2513, 6409,
        2411, 2412, 2414, 2415, 2418, 2421, 2525, 4412, 4415, 4418, 4421, 4424, 6412]

def getCoefficients(naca, reynolds=1e6, iterations=20, angle=10, angle_step=.5):
    xf = XFoil()
    xf.naca(f"{naca:04d}")
    xf.Re = reynolds
    xf.max_iter = 20
    a, cl, cd, cm, cp = xf.aseq(0, angle, .5)
    ratio = cl / cd
    max_idx = np.nanargmax(ratio)
    return (ratio[max_idx], a[max_idx]), a, cl, cd, max_idx

def getBestAirfoil(reynolds=1e6, iterations=20, angle=10):
    liftDragRatio = np.array([getCoefficients(naca, reynolds=reynolds, iterations=iterations, angle=angle)[0] for naca in nacaSet])
    max_idx = np.argmax(liftDragRatio.T[0])
    foil = airfoils.airfoils.Airfoil.NACA4(f"{nacaSet[max_idx]:04d}")
    foil.plot()
    return nacaSet[max_idx], liftDragRatio[max_idx]
