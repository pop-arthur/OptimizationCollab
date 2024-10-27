from objects import *
from typing import Tuple

def input_vars() -> Tuple[Matrix, Matrix, Matrix]:
    """
    Function to input the supply, cost, and demand matrices.
    """
    print('Enter the vector of coefficients of supply  (S):')
    S = Matrix().input(vector_input=True)

    print('Enter the matrix of coefficients of costs (C):')
    C = Matrix().input()

    print('Enter the vector of coefficients of demand(D):')
    D = Matrix().input(vector_input=True)



    return S, C, D
