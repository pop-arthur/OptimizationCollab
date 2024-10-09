def method_is_applicable(simplex_table):
    # degeneracy
    sol_col = simplex_table[0].index("Sol")
    if any(simplex_table[i][sol_col] == 0 for i in range(2, len(simplex_table))):
        return False
    
    return True
    
    