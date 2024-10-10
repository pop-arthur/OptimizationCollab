from typing import Tuple

from objects import *


def input_variables() -> Tuple[Vector, Matrix, Vector, float]:
    """
    Function to get all user input. Return all data in classes and one - in float
    """
    print('First, enter a vector of coefficients for the objective function:')
    vcof = Vector().input()

    print('Now, enter a matrix of coefficients for the constraint function:')
    mccf = Matrix().input()

    print('Next, enter a vector of right-hand side numbers:')
    vrhsn = Vector().input()

    print('Lastly, enter the approximation accuracy:')
    apac = float(input())
    """
    # for dev purpouse only. Delete before prod.
    print("Objective Function Coefficients:", vcof.row)
    print("Constraint Matrix:")
    for row in mccf.matrix:
        print(row)
    print("Right-Hand Side Vector:", vrhsn.row)
    print("Approximation Accuracy:", apac)
    # end of block to be deleted
    """
    return vcof, mccf, vrhsn, apac
