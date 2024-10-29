from transportation_problem.objects.Table import Table
from copy import deepcopy


class RusselTable(Table):
    def __init__(self, table: Table):
        super().__init__(table.supply.copy(), deepcopy(table.costs), table.demand.copy())

    def get_max_in_the_row(self):
        return [max(row) for row in self.costs]

    def get_max_in_the_column(self):
        res = []
        for j in range(len(self.costs[0])):
            res.append(
                max(self.costs[i][j] for i in range(len(self.costs)))
            )
        return res

    def get_solution(self):
        # vector of solution
        solution = []
        while True:
            # get vectors of maximum rows / columns
            row_max, col_max = self.get_max_in_the_row(), self.get_max_in_the_column()
            # if everything is done, then end
            if max(row_max) == 0 and max(col_max) == 0:
                break
            # copy array of costs
            costs = deepcopy(self.costs)
            # calculate cij
            for i in range(len(costs)):
                for j in range(len(costs[0])):
                    if costs[i][j] != 0:
                        costs[i][j] = costs[i][j] - (row_max[i] + col_max[j])

            # choose the most negative value in the table
            x, y = None, None
            value = 10 ** 3
            for i in range(len(costs)):
                for j in range(len(costs[0])):
                    if costs[i][j] < value:
                        x = i
                        y = j
                        value = costs[i][j]
            if value >= 0:
                break
            # subtract demand and supply and add solution
            solution.append(self.process_subtraction(x, y))

        return solution
