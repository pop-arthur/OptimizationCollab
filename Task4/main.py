from utils import *
def func_for_bisec(x: float) -> float: return x**3 -6 * (x**2) + 11 * x - 6 
def func_for_golden(x: float) -> float: return (x-2)**2 + 3
def func_for_gradascent(x: float) -> float: return -(x**2) + 4 * x + 1
def deriv(x: float) -> float: return -2 * x + 4
def main():
    print("Be ready to pass input data for Task 1")
    first_task: tuple[list[float], float] = get_input_root_and_min()
    print("Be ready to pass input data for Task 2")
    second_task: tuple[list[float], float] = get_input_root_and_min()
    print("Be ready to pass input data for Task 3")
    third_task: tuple[list[float], float] = get_input_max()
    print(solveBi(first_task[0], first_task[1], func=func_for_bisec))
    print(solveGolden(second_task[0], second_task[1], func=func_for_golden))
    print(solveGrad(third_task[0], third_task[1], third_task[2], der=deriv, func=func_for_gradascent))


if __name__ == '__main__':
    main()

    