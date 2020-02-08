import csv
import os


#comment
# Set path for file
csvpath = os.path.join("election_data.csv")
# file_to_ouput = "election_analysis.txt"

# file_to_load = "raw_data/election_data.csv"

#print(csvpath)

# Open and read the CSV
with open(csvpath) as csvfile:
    #print(csvreader)
    
    # Read header row, print it, set it aside
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    #print(f"Header: {csv_header}")
 
    #
    Candidates = {}
    Count = 0
    Votes_Cast = 0
    percent_of_votes = 0
    Most_Votes = 0
    Most_Voted = ""
    

    
    for row in csvreader:
        
        # Count the total number of votes cast
        candidate = row[2]
        Count += 1
        if candidate in Candidates.keys():
            Candidates[candidate] += 1
        else:
            Candidates[candidate] = 1
        #print(Candidates)
    
    
    # Print Statements
    print("Election Results")
    print("-------------------------------")
    print(f"Total Votes: {Count}")
    print("-------------------------------")
    
            
    #total number of votes for each candidate
    for candidate in Candidates:
        Votes_Cast += Candidates[candidate]
    
        # percent of votes for each candidate
        percent_of_votes = (Candidates[candidate])/(Count) * 100
        print(f"{candidate}: {int(percent_of_votes)}% {Votes_Cast}")
        
        if Candidates[candidate] > Most_Votes:
            Most_Voted = candidate
            Most_Votes = Candidates[candidate]
        
        
    
    # The winner of the election based on popular vote.
    print("-------------------------------")
    
    print(f"Winner: {Most_Voted}")
    
    print("-------------------------------")





    # Import dependencies
import os, csv
from pathlib import Path 

# Assign file location with the pathlib library
csv_file_path = Path("election_data.csv")

# Declare Variables 
total_votes = 0 
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

# Open csv in default read mode with context manager
with open(csv_file_path,newline="", encoding="utf-8") as elections:

    # Store data under the csvreader variable
    csvreader = csv.reader(elections,delimiter=",") 

    # Skip the header so we iterate through the actual values
    header = next(csvreader)     

    # Iterate through each row in the csv
    for row in csvreader: 

        # Count the unique Voter ID's and store in variable  called total_votes
        total_votes +=1

        # We have four candidates if the name is found, count the times it appears and store in a list
        # We can use this values in our percent vote calculation in the print statements
        if row[2] == "Khan": 
            khan_votes +=1
        elif row[2] == "Correy":
            correy_votes +=1
        elif row[2] == "Li": 
            li_votes +=1
        elif row[2] == "O'Tooley":
            otooley_votes +=1

 # To find the winner we want to make a dictionary out of the two lists we previously created 
candidates = ["Khan", "Correy", "Li","O'Tooley"]
votes = [khan_votes, correy_votes,li_votes,otooley_votes]

# We zip them together the list of candidate(key) and the total votes(value)
# Return the winner using a max function of the dictionary 
dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

# Print a the summary of the analysis
khan_percent = (khan_votes/total_votes) *100
correy_percent = (correy_votes/total_votes) * 100
li_percent = (li_votes/total_votes)* 100
otooley_percent = (otooley_votes/total_votes) * 100

# Print the summary table
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"Khan: {khan_percent:.3f}% ({khan_votes})")
print(f"Correy: {correy_percent:.3f}% ({correy_votes})")
print(f"Li: {li_percent:.3f}% ({li_votes})")
print(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
print(f"----------------------------")
print(f"Winner: {key}")
print(f"----------------------------")