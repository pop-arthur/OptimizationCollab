from utils import *
from objects import *


def main():
    # input data
    supply, cost, demand = input_variables()

    # create transportation table
    table = Table(supply, cost, demand)
    # get solutions
    north_west_solution = NorthwestTable(table).get_solution()
    vogel_solution = VogelTable(table).get_solution()
    russel_solution = RussellTable(table).get_solution()
    # show the table
    table.show()
    # print results
    print(
        "",
        f"North-West Corner method:", north_west_solution,
        f"Vogel’s approximation method:", vogel_solution,
        f"Russell’s approximation method:", russel_solution,
        sep="\n"
    )


if __name__ == '__main__':
    # except possible errors
    try:
        # call main function
        main()
    except ValueError as e:
        print(e)

