def get_solution(simplex_table) -> float:
    solution_col = simplex_table[0].index("Sol")
    return simplex_table[1][solution_col]

def get_vector(simplex_table, length) -> float:
    vcof = [0 for _ in range(length)]
    
    solution_col = simplex_table[0].index("Sol")
    for row in simplex_table:
        if "x" in row[0]:
            vcof[int(row[0].split("_")[1]) - 1] = row[solution_col]
    return tuple(vcof)
