from typing import Callable

def solveBi(interval: list[float], tolerance: float, func: Callable[[float], float]) -> float:
    f_a:float = func(interval[0])
    f_b:float = func(interval[1])
    if (f_a*f_b > 0):
        raise ValueError("f(a) * f(b) must be negative")
    c = (interval[0] + interval[1])/2 #mid point
    f_c : float = func(c)
    if (f_c == 0 or abs(f_c) <= tolerance):
        return c
    if (f_a*f_c >= 0):
        return solveBi([c, interval[1]], tolerance=tolerance, func=func)
    elif (f_b*f_c < 0):
        return solveBi([c, interval[0]], tolerance=tolerance, func=func)
    return 0.0
