from typing import Tuple


def get_input_root_and_min()-> Tuple[list[float], float]:
    interval_str:list[str] = input('Write an interval separate by a space character: ').split(' ')
    interval:list[float] = list(map(float, interval_str))
    tolerance:float = float(input('Write a tolerance: '))
    return interval, tolerance

def get_input_max()-> Tuple[float, float, int]:
    x_0:float = float(input('Write an initial guess: '))
    learning_rate:float = float(input('Write a learning rate: '))
    number_of_iterations:int = int(input('Write a number of iterations: '))
    return x_0, learning_rate, number_of_iterations