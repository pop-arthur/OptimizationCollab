def input_variables():
    supply = list(map(int, input().split()))
    costs = [list(map(int, input().split())) for _ in range(len(supply))]
    demand = list(map(int, input().split()))
    if len(supply) != len(costs) or any(len(demand) != len(costs[i]) for i in range(len(costs))):
        raise IndexError('Invalid size')
    if sum(supply) != sum(demand):
        raise ValueError("Sum demand != Sum supply")
    return supply, costs, demand