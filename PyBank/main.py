# Modules
import os
import csv

# Set path for file
csvpath = os.path.join ("budget_data.csv")

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

max_change_month = monthly_change.index(max(monthly_change)) + 1
min_change_month = monthly_change.index(min(monthly_change)) + 1 

# Define variables to Print
lengh = len(profits)
total_profits = sum(profits)
ave_change = round(sum(monthly_change)/len(monthly_change),2)

# Print results
line1 = print("Financial Analysis")
line2 = print("----------------------------")
print("Total Months: " + str(lengh))
print("Total: $" + str(total_profits))
print("Average Change: " + str(ave_change))
print("Greatest Increase in Profits: " + months[max_change_month] + " ($" + str(max_monthly_change) + ")")
print("Greatest Decrease in Profits: " + months[min_change_month] + " ($" + str(min_monthly_change) + ")")

# Create output file and open it for writing
output_file = os.path.join("Financial_Analysis_Summary.txt")

with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

# Write methods to print to Financial_Analysis_Summary 
    datafile.write("Financial Analysis")
    datafile.write("\n")
    datafile.write("----------------------------")
    datafile.write("\n")
    datafile.write("Total Months: " + str(lengh))
    datafile.write("\n")
    datafile.write("Total: $" + str(total_profits))
    datafile.write("\n")
    datafile.write("Average Change: " + str(ave_change))
    datafile.write("\n")
    datafile.write("Greatest Increase in Profits: " + months[max_change_month] + " ($" + str(max_monthly_change) + ")")
    datafile.write("\n")
    datafile.write("Greatest Decrease in Profits: " + months[min_change_month] + " ($" + str(min_monthly_change) + ")")