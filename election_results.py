# Modules
import os
import csv

# Set path for file
csvpath = os.path.join ("Resources/election_data.csv")

# Open file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

# Empty dictionary to save values from csv file
    candidates = {}

# Save values of candidates in the dictionary
    for rows in csvreader:
        votes = rows[2]

        if votes in candidates.keys():
            candidates[votes] += 1
        else:
            candidates[votes] = 1

    total_votes = sum(candidates.values())

# Determine the winner
    winner = max([(value, key) for key, value in candidates.items()])[1]        

# Generate strings to print 
    string1 = f'Election Results \n\
----------------------------\n\
Total Votes {str(total_votes)} \n\
----------------------------'
    string2 = f'----------------------------\n\
Winner: {str(winner)}\n\
----------------------------'

# Print results
    print(string1)
    for k,v in candidates.items():
        print(f"{k}: {round((v/total_votes * 100),0)}% ({format(v,',')})" )
    print(string2)

# Create output file and open it for writing
output_file = os.path.join("Results/Election Results.txt")

with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

# Write methods to print to Election Results 
    datafile.write(string1)
    for k,v in candidates.items():
        datafile.write(f"{k}: {round((v/total_votes * 100),0)}% ({format(v,',')})" )
    datafile.write(string2)