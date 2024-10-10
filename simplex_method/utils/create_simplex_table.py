from typing import List, Any

from objects import *


def create_simplex_table(vcof: Vector, mccf: Matrix, vrhsn: Vector) -> List[List[Any]]:
    # create table
    simplex_table = [
        [0 for _ in range(vcof.numb_of_columns + mccf.numb_of_rows + 3)] for _ in range(mccf.numb_of_rows + 2)
    ]

    # multiply vector of function coefficients by -1
    vcof.multiply_by(-1)

    # name rows
    simplex_table[0][0] = "---"
    for i in range(vcof.numb_of_columns):
        simplex_table[0][i + 1] = f"x_{i + 1}"
    for i in range(mccf.numb_of_rows):
        simplex_table[0][i + vcof.numb_of_columns + 1] = f"s_{i + 1}"
    simplex_table[0][-2] = "Sol"
    simplex_table[0][-1] = "Rat"

    # name columns
    simplex_table[1][0] = "z"
    for j in range(mccf.numb_of_rows):
        simplex_table[j + 2][0] = f"s_{j + 1}"

    # add z func to the table
    for i in range(vcof.numb_of_columns):
        simplex_table[1][i + 1] = vcof[i]

    # add constrains
    for i in range(mccf.numb_of_rows):
        # define x
        simplex_table[i + 2][1:mccf.numb_of_columns + 1] = mccf.matrix[i]
        # define slack variable
        slack_column = simplex_table[0].index(f"s_{i+1}")
        simplex_table[i + 2][slack_column] = 1
        # define solution
        simplex_table[i + 2][-2] = vrhsn[i]
        # edit ratio
        simplex_table[i + 2][-1] = "-"


    return simplex_table
