from simplex_method.utils.choose_pivots import choose_pivot_element
from simplex_method.utils.compute_new_table import compute_new_simplex_table
from utils import *
from tabulate import tabulate
from decimal import Decimal, ROUND_HALF_UP

def round_with_precision(value, precision):
    decimal_value = Decimal(value).quantize(Decimal(f"1.{'0' * precision}"), rounding=ROUND_HALF_UP)
    return float(decimal_value)

def round_table(table, apac):
    apac = int(apac)
    for i in range(1, len(table)):
        for j in range(1, len(table[i])):
            if isinstance(table[i][j], (int, float)):
                table[i][j] = round_with_precision(table[i][j], apac)
    return table

if __name__ == '__main__':
    # Get user input
    vcof, mccf, vrhsn, apac = input_variables()
    # Write great phrase! :)
    print("Welcome to Hell!")
    # create simplex table based on input
    simplex_table = create_simplex_table(vcof, mccf, vrhsn)
    print(tabulate(simplex_table))
    while True:
        # Check if all elements in the z-line are non-negative
        if all(x >= 0 for x in simplex_table[1][1:]):
            break
        tbl, piv_row_ind, piv_col_ind = choose_pivot_element(simplex_table)
        print(tabulate(tbl))
        # Compute the new simplex table
        updated_table = compute_new_simplex_table(tbl, piv_row_ind, piv_col_ind)
        print(tabulate(updated_table))
        simplex_table = updated_table

    final_table = round_table(simplex_table, apac)
    print("\nFinal Simplex Table (rounded to inputed accuracy):")
    print(tabulate(final_table))
