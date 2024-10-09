def compute_new_simplex_table(simplex_table, piv_row_ind, piv_col_ind):
    # Extract the new pivot row that was already updated
    new_pivot_row = simplex_table[piv_row_ind]

    # Iterate over all rows except the pivot row
    for i in range(1, len(simplex_table)):
        if i == piv_row_ind:
            continue

        # Get the coefficient of the current row at the pivot column
        pivot_column_coef = simplex_table[i][piv_col_ind]

        # Update each element of the current row using the formula:
        for j in range(1, len(simplex_table[i])-1):
            simplex_table[i][j] = simplex_table[i][j] - pivot_column_coef * new_pivot_row[j]


    return simplex_table
