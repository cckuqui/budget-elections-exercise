# Modules
import os
import csv

# Set path for file
csvpath = os.path.join ("election_data.csv")

# Open file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

# Empty dictionary to save values from csv file
    candidates = {}

# Define variables to store counts of total votes and for each candidate
    total_votes = 0

# Save values of candidates in dictionary
    for rows in csvreader:
        votes = rows[2]
        total_votes +=1

        if votes in candidates.keys():
            candidates[votes] += 1
        else:
            candidates[votes] = 1

print(candidates)

# Add value in percentage


# Print results
print("Election Results")
print("----------------------------")
print("Total Votes: " + str(total_votes))
print("----------------------------")
# print("Total: $" + str(total_profits))
# print("Average Change: " + str(ave_change))
# print("Greatest Increase in Profits: " + months[max_change_month] + " ($" + str(max_monthly_change) + ")")
# print("Greatest Decrease in Profits: " + months[min_change_month] + " ($" + str(min_monthly_change) + ")")

# # Create output file and open it for writing
# output_file = os.path.join("Financial_Analysis_Summary.txt")

# with open(output_file, "w", newline="") as datafile:
#     writer = csv.writer(datafile)

# # Write methods to print to Financial_Analysis_Summary 
#     datafile.write("Financial Analysis")
#     datafile.write("\n")
#     datafile.write("----------------------------")
#     datafile.write("\n")
#     datafile.write("Total Months: " + str(lengh))
#     datafile.write("\n")
#     datafile.write("Total: $" + str(total_profits))
#     datafile.write("\n")
#     datafile.write("Average Change: " + str(ave_change))
#     datafile.write("\n")
#     datafile.write("Greatest Increase in Profits: " + months[max_change_month] + " ($" + str(max_monthly_change) + ")")
#     datafile.write("\n")
#     datafile.write("Greatest Decrease in Profits: " + months[min_change_month] + " ($" + str(min_monthly_change) + ")")