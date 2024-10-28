from transportation_problem.objects.VogelTable import VogelTable
from utils import *
from objects import *


def main():
    supply, cost, demand = input_variables()

    table = Table(supply, cost, demand)
    table.show()
    print(
        "",
        f"North-West Corner method: {NorthwestTable(table).get_solution()}",
        f"Vogel’s approximation method: {VogelTable(table).get_solution()}",
        sep="\n"
    )


if __name__ == '__main__':
    main()