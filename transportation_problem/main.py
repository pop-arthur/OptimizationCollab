from utils import *
from objects import *


def main():
    # input data
    supply, cost, demand = input_variables()

    # create transportation table
    table = Table(supply, cost, demand)
    # show the table
    table.show()
    # print results
    print(
        "",
        f"North-West Corner method:", NorthwestTable(table).get_solution(),
        f"Vogel’s approximation method:", VogelTable(table).get_solution(),
        f"Russell’s approximation method:", RussellTable(table).get_solution(),
        sep="\n"
    )


if __name__ == '__main__':
    # except possible errors
    try:
        # call main function
        main()
    except ValueError as e:
        print(e)

