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
        # candidates["percentage"]
        string = f"{k}: {round((v/total_votes * 100),3)}00% ({v})"
        print(string)
    
    inverse_dictionary = [(value, key) for key, value in candidates.items()]
    
    print("----------------------------")
    print("Winner: " + str(max(inverse_dictionary)[1]))
    print("----------------------------")
 
# Create output file and open it for writing
output_file = os.path.join("Election Results.txt")

with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

# Write methods to print to Election Results 
    datafile.write("Election Results")
    datafile.write("\n")
    datafile.write("----------------------------")
    datafile.write("\n")
    datafile.write("Total Votes: " + str(total_votes))
    datafile.write("\n")
    datafile.write("----------------------------")
    datafile.write("\n")
    for k,v in candidates.items():
        string = f"{k}: {round((v/total_votes * 100),3)}00% ({v})\n"
        datafile.write(string)
    datafile.write("----------------------------")
    datafile.write("\n")
    datafile.write("Winner: " + str(max(inverse_dictionary)[1]))
    datafile.write("\n")
    datafile.write("----------------------------")