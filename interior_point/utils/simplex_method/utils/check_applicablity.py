def method_is_applicable(simplex_table):
    # degeneracy
    sol_col = simplex_table[0].index("Sol")
    if any(simplex_table[i][sol_col] == 0 for i in range(2, len(simplex_table))):
        return False
    
    # equal ratio
    ratios = [row[-1] for row in simplex_table[2:] if row != "-"]
    if ratios.count(min(ratios)) != 1:
        return False
    return True
    
    