import itertools

# List of actions with their costs and profits
actions = [
    {"name": "Action-1", "cost": 20, "profit": 0.05},
    {"name": "Action-2", "cost": 30, "profit": 0.10},
    {"name": "Action-3", "cost": 50, "profit": 0.15},
    {"name": "Action-4", "cost": 70, "profit": 0.20},
    {"name": "Action-5", "cost": 60, "profit": 0.17},
    {"name": "Action-6", "cost": 80, "profit": 0.25},
    {"name": "Action-7", "cost": 22, "profit": 0.07},
    {"name": "Action-8", "cost": 26, "profit": 0.11},
    {"name": "Action-9", "cost": 48, "profit": 0.13},
    {"name": "Action-10", "cost": 34, "profit": 0.27},
    {"name": "Action-11", "cost": 42, "profit": 0.17},
    {"name": "Action-12", "cost": 110, "profit": 0.09},
    {"name": "Action-13", "cost": 38, "profit": 0.23},
    {"name": "Action-14", "cost": 14, "profit": 0.01},
    {"name": "Action-15", "cost": 18, "profit": 0.03},
    {"name": "Action-16", "cost": 8, "profit": 0.08},
    {"name": "Action-17", "cost": 4, "profit": 0.12},
    {"name": "Action-18", "cost": 10, "profit": 0.14},
    {"name": "Action-19", "cost": 24, "profit": 0.21},
    {"name": "Action-20", "cost": 114, "profit": 0.18},
]

# Maximum budget per client
max_budget = 500

# Function to calculate the total profit for a combination of actions
def calculate_total_profit(combination):
    total_cost = sum(actions[i]["cost"] for i in combination)
    total_profit = sum(actions[i]["profit"] for i in combination)
    return total_cost, total_profit

best_profit = 0
best_combination = []

# Iterate through all possible combinations of actions
for r in range(1, len(actions) + 1):
    for combination in itertools.combinations(range(len(actions)), r):
        total_cost, total_profit = calculate_total_profit(combination)
        if total_cost <= max_budget and total_profit > best_profit:
            best_profit = total_profit
            best_combination = combination

# Print the best combination and the corresponding profit
print("Best combination of actions:")
for i in best_combination:
    print(actions[i]["name"])
print("Total profit after 2 years: {:.2f} euros".format(best_profit * max_budget))