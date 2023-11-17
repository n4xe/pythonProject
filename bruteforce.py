from functions import read_actions_from_file
from functions import find_best_combination
import time

start_time = time.time()

actions = read_actions_from_file("actions.txt")
max_budget = 500

# Find the best combination
best_combination, best_profit = find_best_combination(actions, max_budget)

end_time = time.time()

# Print the best combination and the corresponding profit
print("Best combination of actions:")
for i in best_combination:
    print(actions[i]["name"])
print("Total profit after 2 years: {:.2f} euros".format(best_profit))

# Print the elapsed time
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time} seconds")