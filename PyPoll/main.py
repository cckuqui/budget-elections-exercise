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

# Fuction of candidate list with votes and percentages
    def candidate():
        for k,v in candidates.items():
            yield f"{k}: {round((v/total_votes * 100),0)}% ({format(v,',')})" 

# Generate string with a list of candidates and their results 
    whole_string = f'Election Results \n\
----------------------------\n\
Total Votes {str(total_votes)} \n\
----------------------------\n\
{candidate()}\n\
----------------------------\n\
Winner: {str(winner)}\n\
----------------------------'

# Print results
    print(whole_string)
 
# Create output file and open it for writing
output_file = os.path.join("Election Results.txt")

with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

# Write methods to print to Election Results 
    datafile.write(whole_string)