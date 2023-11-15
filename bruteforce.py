def read_actions_from_file(filename):
    actions = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            name = parts[0]
            cost = int(parts[1])
            profit_percentage = float(parts[2].replace('%', '')) / 100.0
            actions.append({"name": name, "cost": cost, "profit": profit_percentage})
    return actions

def calculate_total_profit(combination, actions):
    total_cost = sum(actions[i]["cost"] for i in combination)
    total_profit_percentage = sum(actions[i]["profit"] for i in combination)
    total_profit = total_cost * total_profit_percentage
    return total_cost, total_profit

def find_best_combination(actions, max_budget):
    best_combination = []
    best_profit = 0.0

    num_actions = len(actions)

    # Try all possible combinations using a bitmask
    for bitmask in range(1, (1 << num_actions)):
        current_combination = [i for i in range(num_actions) if (bitmask & (1 << i)) > 0]
        total_cost, total_profit = calculate_total_profit(current_combination, actions)

        if total_cost <= max_budget and total_profit > best_profit:
            best_profit = total_profit
            print(best_profit)
            best_combination = current_combination[:]
            print(best_combination)

    return best_combination, best_profit

if __name__ == "__main__":
    # Read actions from the file
    actions = read_actions_from_file("actions.txt")

    # Maximum budget per client
    max_budget = 500

    # Find the best combination
    best_combination, best_profit = find_best_combination(actions, max_budget)

    # Print the best combination and the corresponding profit
    print("Best combination of actions:")
    for i in best_combination:
        print(actions[i]["name"])
    print("Total profit after 2 years: {:.2f} euros".format(best_profit))
