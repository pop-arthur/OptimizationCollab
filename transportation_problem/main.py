from utils import *
from objects import *


def main():
    supply, cost, demand = input_variables()

    table = Table(supply, cost, demand)
    table.show()
    print(
        "",
        f"North-West Corner method:\n{NorthwestTable(table).get_solution()}",
        f"Vogel’s approximation method:\n{VogelTable(table).get_solution()}",
        f"Russell’s approximation method:\n{RusselTable(table).get_solution()}",
        sep="\n"
    )


if __name__ == '__main__':
    try:
        main()
    except ValueError as e:
        print(e)

