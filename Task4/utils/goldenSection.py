
from math import sqrt
from typing import Callable

def solveGolden(interval: list[float], tolerance: float, func: Callable[[float], float]) -> tuple[float, float]:
    ratio:float = (sqrt(5) - 1)/2.0
    x1:float = interval[1] - ratio * (interval[1] - interval[0])
    x2:float = interval[0] + ratio * (interval[1] - interval[0])
    f_1:float = func(x1)
    f_2:float = func(x2)
    c = (interval[0] + interval[1])/2 #mid point
    if (abs(interval[0] - interval[1]) < tolerance):
        return c, func(c)
    if (f_1 < f_2):
        return solveGolden([interval[0], x2], tolerance=tolerance, func=func)
    elif (f_1 >= f_2):
        return solveGolden([x1, interval[1]], tolerance=tolerance, func=func)
    return 0.0, 0.0
