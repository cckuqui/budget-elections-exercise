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

# Save values of candidates in dictionary
    for rows in csvreader:
        votes = rows[2]

        if votes in candidates.keys():
            candidates[votes] += 1
        else:
            candidates[votes] = 1

    total_votes = sum(candidates.values())

# Print results
    print("Election Results")
    print("----------------------------")
    print("Total Votes: " + str(total_votes))
    print("----------------------------")

    for k,v in candidates.items():
        print(k + ":",round(v/total_votes*100,3), "%","(" + str(v) + ")")

    print("----------------------------")
    print("Total Votes: " + str(total_votes))
    print("----------------------------")
   


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