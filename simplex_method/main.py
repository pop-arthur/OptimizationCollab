from utils import *
from tabulate import tabulate


NOT_APPLICABLE_MESSAGE = "The method is not applicable!"


def simplex_method():
    # Get user input
    vcof, mccf, vrhsn, apac = input_variables()
    
    # check number of variables greater or equal to number of constrains
    if vcof.numb_of_columns < vrhsn.numb_of_columns:
        print(NOT_APPLICABLE_MESSAGE)
        return
    
    # create simplex table based on input
    simplex_table = create_simplex_table(vcof, mccf, vrhsn)
    print(tabulate(simplex_table))
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
        # print(tabulate(updated_table))
        simplex_table = updated_table
        print(tabulate(simplex_table))

    final_table = round_table(simplex_table, apac)
    # print("\nFinal Simplex Table (rounded to inputed accuracy):")
    # print(tabulate(final_table))
    print("A vector of decision variables:", get_vector(final_table, vcof.numb_of_columns))
    print("Maximum value of the objective function:", get_solution(final_table))
    
    
if __name__ == '__main__':
    simplex_method()
