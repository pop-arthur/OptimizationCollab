import math

from ..objects import *


def choose_pivot_element(simplex_table):
    # calculate ratio
    piv_col_ind = simplex_table[1].index(min(simplex_table[1][1:-2]))
    for i in range(2, len(simplex_table)):
        if (simplex_table[i][piv_col_ind] == 0):
            simplex_table[i][-1] = 0
            continue
        simplex_table[i][-1] = simplex_table[i][-2] / simplex_table[i][piv_col_ind]

    # selecting appropriate ratios
    ratios = []
    for i in range(1, len(simplex_table)):
        el = simplex_table[i][-1]
        if el <= 0:
            ratios.append(math.inf)
        else:
            ratios.append(el)

    piv_row_ind = ratios.index(min(ratios)) + 1
    pivot_el = simplex_table[piv_row_ind][piv_col_ind]

    # creating new pivot row
    new_pivot_row = [simplex_table[0][piv_col_ind]]
    for i in range(1, len(simplex_table[piv_row_ind])):
        if i != len(simplex_table[piv_row_ind]) - 1:
            new_pivot_row.append(simplex_table[piv_row_ind][i] / pivot_el)
        else:
            new_pivot_row.append(simplex_table[piv_row_ind][i])

    # changing the old pivot row to new one
    simplex_table[piv_row_ind] = new_pivot_row
    return simplex_table, piv_row_ind, piv_col_ind
