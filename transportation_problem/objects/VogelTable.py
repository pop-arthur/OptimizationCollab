from transportation_problem.objects.Table import Table
from copy import deepcopy


class VogelTable(Table):
    def __init__(self, table: Table):
        super().__init__(table.supply.copy(), deepcopy(table.costs), table.demand.copy())

    def get_rows_delta(self):
        delta_rows = []
        for i in range(len(self.costs)):
            sorted_row = list(filter(lambda x: x != 0, sorted(self.costs[i])))
            if len(sorted_row) >= 2:
                delta_rows.append(sorted_row[1] - sorted_row[0])
            elif len(sorted_row) == 1:
                delta_rows.append(1)
            else:
                delta_rows.append(0)

        return delta_rows

    def get_columns_delta(self):
        delta_columns = []
        for j in range(len(self.costs[0])):
            sorted_column = sorted([self.costs[i][j] for i in range(len(self.costs)) if self.costs[i][j] != 0])
            if len(sorted_column) >= 2:
                delta_columns.append(sorted_column[1] - sorted_column[0])
            elif len(sorted_column) == 1:
                delta_columns.append(1)
            else:
                delta_columns.append(0)
        return delta_columns

    def get_solution(self):
        # vector of solution
        solution = []
        while True:
            # get maximum difference between two min numbers
            rows_delta = self.get_rows_delta()
            max_delta_row = max(rows_delta)
            columns_delta = self.get_columns_delta()
            max_delta_column = max(columns_delta)

            # if end reached
            if max_delta_row == max_delta_column == 0:
                break
            # if maximum difference in row
            elif max_delta_row >= max_delta_column:
                # get number of row with maximum difference
                row_number = rows_delta.index(max_delta_row)
                # get coordinates of minimum cell in the row
                x, y = row_number, self.costs[row_number].index(
                    min(list(filter(lambda t: t != 0, self.costs[row_number])))
                )
            # if maximum difference in column
            else:
                # get number of column with maximum difference
                column_number = columns_delta.index(max_delta_column)
                # column numbers
                column_numbers = [self.costs[i][column_number] for i in range(len(self.costs))]
                # get coordinates of cell
                x, y = column_numbers.index(
                    min(list(filter(lambda t: t != 0, column_numbers)))
                ), column_number

            print(x, y)
            # subtract demand and supply and add solution
            solution.append(self.process_subtraction(x, y))

        return solution
