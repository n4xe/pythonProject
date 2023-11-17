from itertools import combinations
import csv


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

    for r in range(1, num_actions + 1):
        # Generate all combinations of length r
        for current_combination in combinations(range(num_actions), r):
            # print(current_combination)
            total_cost, total_profit = calculate_total_profit(current_combination, actions)

            if total_cost <= max_budget and total_profit > best_profit:
                best_profit = total_profit
                print(best_profit)
                best_combination = list(current_combination[:])
                print(best_combination)

    return best_combination, best_profit

def read_actions_from_file_optimized(filename):
    actions = []
    with open(filename, 'r', newline='') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            name = row['name']
            cost = float(row['price'])  # Convert price to float
            profit_percentage = float(row['profit']) / 100.0
            actions.append({"name": name, "cost": cost, "profit": profit_percentage})
    return actions

def find_best_combination_optimized(actions, max_budget):
    best_combination = []
    best_profit = 0.0

    num_actions = len(actions)

    # Try all possible combinations without using a bitmask
    for r in range(1, num_actions + 1):
        # Generate all combinations of length r
        for current_combination in combinations(range(num_actions), r):
            total_cost, total_profit = calculate_total_profit(current_combination, actions)

            # Check if the current combination is within budget and has potential for better profit
            if total_cost <= max_budget and total_profit > best_profit:
                best_profit = total_profit
                best_combination = list(current_combination[:])
                print(best_profit)
                print(best_combination)

    return best_combination, best_profit if best_combination else (None, 0.0)