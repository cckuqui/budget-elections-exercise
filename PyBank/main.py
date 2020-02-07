# Modules
import os
import csv

# Set path for file
csvpath = os.path.join ("budget_data.csv")

# Open file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# Skip header
    data = next(csvreader)
    total_rows = len(data)

# New list
    last_profit = 0
    max_profit = 0
    min_profit = 0

# Add data to lists
    # for rows in csvreader:
        # month.append(rows[0])
        # profit.append(int(rows[1]))
    
    print(total_rows)

    # lenght = len(profit)

    # sum_total = sum(profit)
# print(sum_total)
