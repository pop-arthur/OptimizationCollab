from transportation_problem.objects.Table import Table
from copy import deepcopy


class NorthwestTable(Table):
    def __init__(self, table: Table):
        super().__init__(table.supply.copy(), deepcopy(table.costs), table.demand.copy())

    def find_non_empty_northwest_cell(self):
        for i in range(len(self.costs)):
            for j in range(len(self.costs[i])):
                if self.costs[i][j] != 0:
                    return i, j
        return None, None

    def get_solution(self):
        # vector of solution
        solution = []
        while True:
            # get northwest non-empty cell
            x, y = self.find_non_empty_northwest_cell()
            # end if cell is not found
            if (x, y) == (None, None):
                break

            # subtract demand and supply and add solution
            solution.append(self.process_subtraction(x, y))

        # return found solution
        return solution
