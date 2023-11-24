from functions import read_actions_from_file_optimized
from functions import find_best_combination_optimized2
import time

# Record the start time
start_time = time.time()

# Read actions from the file
actions = read_actions_from_file_optimized("data/dataset1_Python+P7.csv")

# Maximum budget per client
max_budget = 500

# Find the best combination using dynamic programming
best_combination, best_profit = find_best_combination_optimized2(actions, max_budget)

# Record the end time
end_time = time.time()

# Print the elapsed time
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time} seconds")

# Print the best combination and the corresponding profit
print("Best combination of actions:")
for i in best_combination:
    print(actions[i]["name"])
print("Total profit after 2 years: {:.2f} euros".format(best_profit))