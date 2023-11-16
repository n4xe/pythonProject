from functions import read_actions_from_file
from functions import find_best_combination

actions = read_actions_from_file("actions.txt")
max_budget = 500

# Find the best combination
best_combination, best_profit = find_best_combination(actions, max_budget)

# Print the best combination and the corresponding profit
print("Best combination of actions:")
for i in best_combination:
    print(actions[i]["name"])
print("Total profit after 2 years: {:.2f} euros".format(best_profit))
