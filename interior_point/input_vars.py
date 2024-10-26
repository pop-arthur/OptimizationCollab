from objects import *
from typing import Tuple

def input_vars() -> Tuple[Matrix, Matrix, Matrix, Matrix, float]:
    print('Enter the vector of coefficients for the objective function (C):')
    vcof = Matrix().input()

    print('Enter the matrix of coefficients for the constraint function (A):')
    mccf = Matrix().input()

    print('Enter your initial starting point (as a vector):')
    inix = Matrix().input()

    print('Enter the vector of right-hand side numbers (b):')
    vrhsn = Matrix().input()

    print('Enter the approximation accuracy (ϵ):')
    apac = float(input("Accuracy ε: "))

    return vcof, mccf, inix, vrhsn, apac
