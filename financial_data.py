# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("Resources/budget_data.csv")

# Open file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

# Empty list to save values from csv file
    months = []
    profits = []
    monthly_change = []

# Save values into months and profits (as an integer) lists
    for row in csvreader: 
        months.append(row[0])
        profits.append(int(row[1]))

# Calculate differences in profits and save info in monthly_change list
    for i in range(len(profits)-1):
        monthly_change.append(profits[i+1]-profits[i])

    # print(monthly_change)

# Get max and min values from monthly_change list and relate it to month list
max_monthly_change = max(monthly_change)
min_monthly_change = min(monthly_change)

max_change_month = monthly_change.index(max_monthly_change) + 1
min_change_month = monthly_change.index(min_monthly_change) + 1 

# Define variables to Print
length = len(profits)
total_profits = format(sum(profits),'11,')
ave_change = format(sum(monthly_change)/len(monthly_change),'9,.2f')

# Print results
results = f'Financial Analysis\n\
----------------------------\n\
Total Months: {str(length)}\n\
Total: ${str(total_profits)}\n\
Average Change: {str(ave_change)}\n\
Greatest Increase in Profits: {months[max_change_month]} (${str(format(max(monthly_change),"10,.0f"))})\n\
Greatest Decrease in Profits: {months[min_change_month]} (${str(format(min(monthly_change),"10,.0f"))})'

print(results)


# Create output file and open it for writing
output_file = os.path.join("Results/Financial Analysis.txt")

with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

# Write methods to print to Financial Analysis 
    datafile.write(results)