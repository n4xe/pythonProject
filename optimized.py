from functions import read_actions_from_file_optimized
from functions import find_best_combination_optimized
from functions import read_actions_from_file
import time

start_time = time.time()

# Read actions from the file
actions = read_actions_from_file_optimized("data/dataset1_Python+P7.csv")
#actions = read_actions_from_file("actions.txt")

# Sort actions by cost-to-benefit ratio
sorted_actions = sorted(actions, key=lambda x: x["cost"] / x["profit"] if x["profit"] != 0 else float('inf'), reverse=True)

max_budget = 500

# Find the best combination using sorted actions
best_combination, best_profit = find_best_combination_optimized(sorted_actions, max_budget)

end_time = time.time()

# Print the elapsed time
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time} seconds")

# Print the best combination and the corresponding profit
print("Best combination of actions:")
for i in best_combination:
    print(sorted_actions[i]["name"])
print("Total profit after 2 years: {:.2f} euros".format(best_profit))
