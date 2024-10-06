from simplex_method.utils.choose_pivots import choose_pivot_element
from simplex_method.utils.compute_new_table import compute_new_simplex_table
from utils import *
from tabulate import tabulate


if __name__ == '__main__':
    # Get user input
    vcof, mccf, vrhsn, apac = input_variables()
    # Write great phrase! :)
    print("Welcome to Hell!")
    # create simplex table based on input
    simplex_table = create_simplex_table(vcof, mccf, vrhsn, apac)
    print(tabulate(simplex_table))
    tbl, piv_row_ind, piv_col_ind = choose_pivot_element(simplex_table)
    print(tabulate(tbl))
    # Compute the new simplex table
    updated_table = compute_new_simplex_table(tbl, piv_row_ind, piv_col_ind)
    print(tabulate(updated_table))
    tbl2, piv_row_ind2, piv_col_ind2 = choose_pivot_element(updated_table)
    print(tabulate(tbl2))

