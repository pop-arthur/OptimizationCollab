from simplex_method.utils.choose_pivots import choose_pivot_element
from utils import *


if __name__ == '__main__':
    # Get user input
    vcof, mccf, vrhsn, apac = input_variables()
    # Write great phrase! :)
    print("Welcome to Hell!")
    # create simplex table based on input
    simplex_table = create_simplex_table(vcof, mccf, vrhsn, apac)
    tbl, piv_row_ind, piv_col_ind = choose_pivot_element(simplex_table)
    from tabulate import tabulate
    #print(tabulate(simplex_table))
    print(tabulate(tbl))

