from xfoil import XFoil

nacaSet = [6, 7, 9, 10, 12, 15, 18, 21, 24, 1408, 1410, 1412, 2408, 2410, 2513, 6409
        2411, 2412, 2414, 2415, 2418, 2421, 2525, 4412, 4415, 4418, 4421, 4424, 6412]

def getCoefficients(naca, reynolds=1e6, iterations=10):
    xf = XFoil()
    xf.naca(f"{naca:04d}")
    xf.Re = reynolds
    xf.max_iter = iterations
    a, cl, cd, cm, cp = xf.aseq(-20, 20, 2)
    ratio = cl / cd
    min_idx = ratio.argsort()[0]
    return (ratio[min_idx], a[min_idx])

def getBestAirfoil(reynolds=1e6):
    liftDragRatio = np.array([getCoefficients(naca) for naca in nacaSet])


