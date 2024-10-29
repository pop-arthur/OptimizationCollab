from tabulate import tabulate


# class representing transportation table
class Table:
    def __init__(self, supply, costs, demand):
        """
        :param supply: vector of supply
        :param costs: matrix of costs
        :param demand: vector of demand
        """
        self.table = [
            [*costs[i], supply[i]] for i in range(len(supply))
        ] + [[*demand, sum(demand)]]

        self.supply = supply
        self.costs = costs
        self.demand = demand

    def __str__(self):
        return str(self.table)

    def show(self):
        print(
            tabulate(
                self.table,
                headers=[*[f"B{i + 1}" for i in range(len(self.table[0]) - 1)], "Supply"],
                showindex=[f"A{i + 1}" for i in range(len(self.table) - 1)] + ["Demand"],
            )
        )

    # abstract method that should be defined in subclasses
    def get_solution(self):
        pass

    def process_subtraction(self, x, y):
        """
        method that process operations over table when solution is defined
        :param x: x coordinate of solution
        :param y: y coordinate of solution
        :return: solution string
        """
        # get possible amount
        amount = min(self.supply[x], self.demand[y])
        # get price of transportation
        price = self.costs[x][y]
        # add cell to the solution vector
        # subtract cell, supply and demand
        self.costs[x][y] = 0
        self.supply[x] -= amount
        self.demand[y] -= amount
        # process null supply
        if self.supply[x] == 0:
            for j in range(len(self.costs[x])):
                self.costs[x][j] = 0
        # process null demand
        if self.demand[y] == 0:
            for i in range(len(self.costs)):
                self.costs[i][y] = 0
        return f"{amount} * A{x + 1}B{y + 1} ({price})"
