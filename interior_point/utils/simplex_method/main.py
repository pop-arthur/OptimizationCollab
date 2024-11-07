from typing import Tuple
from .utils.input_variables import input_variables
from .utils import *
from .objects.Matrix import Matrix
from .objects.Vector import Vector
# from tabulate import tabulate #TODO: What is this for?


NOT_APPLICABLE_MESSAGE = "The method is not applicable!"


def simplex_method(vcof: Vector, mccf: Matrix, vrhsn:Vector, apac:float):
    # Get user input
    # vcof, mccf, vrhsn, apac = input_variables()
    # print(type(vcof), type(mccf), type(vrhsn), type(apac)) #For debugging purposes only
    if not (isinstance(vcof, Vector) and isinstance(mccf, Matrix) and isinstance(vrhsn, Vector)):
        raise ValueError("All inputs must be Vector and Matrix instances. Проще говоря пошёл нахуй")
    # print(isinstance(vcof, Vector)) #For debugging purposes only
    # print(vcof.numb_of_columns) #For debugging purposes only 
    # check number of variables greater or equal to number of constrains
    if vcof.numb_of_columns < vrhsn.numb_of_columns:
        print(NOT_APPLICABLE_MESSAGE)
        return
    
    # create simplex table based on input
    simplex_table = create_simplex_table(vcof, mccf, vrhsn)
    while True:
        # Check if all elements in the z-line are non-negative
        if all(x >= 0 for x in simplex_table[1][1:]):
            break
        tbl, piv_row_ind, piv_col_ind = choose_pivot_element(simplex_table)
        
        # check applicabilty
        if not method_is_applicable(tbl):
            print(NOT_APPLICABLE_MESSAGE)
            return
        
        # Compute the new simplex table
        updated_table = compute_new_simplex_table(tbl, piv_row_ind, piv_col_ind)
        simplex_table = updated_table

    final_table = round_table(simplex_table, apac)
    # print("\nFinal Simplex Table (rounded to inputed accuracy):")
    # print(tabulate(final_table))
    print("A vector of decision variables:", get_vector(final_table, vcof.numb_of_columns))
    print("Maximum value of the objective function:", get_solution(final_table))
    
    
if __name__ == '__main__':
    vcof:Vector = Vector()
    mccf:Matrix = Matrix()
    vrhsn:Vector = Vector()
    apac:float = 0.0001  # accuracy of the solution
    Tuple[vcof: Vector, mccf:Matrix, vrhsn:Vector, apac:float] = input_variables()
    simplex_method(vcof, mccf, vrhsn, apac)
