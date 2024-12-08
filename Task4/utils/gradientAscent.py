from typing import Callable

def solveGrad(init_guess:float, learning_rate: float, itter: int, der: Callable[[float], float], func: Callable[[float], float]) -> tuple[float, float]:
    for i in range(itter) :
        init_guess += learning_rate*der(init_guess)
    return init_guess, func(init_guess)