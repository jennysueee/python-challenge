#importing & setting up paths
import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")
output = os.path.join("Resources", "analysis.txt")

# Set variables
Candidates = []
Candidate_Votes = []
Count = 0
Number_of_Votes = 0
Percent_of_votes = 0
Votes_Per_Candidate = []
Winner = ""
    
# Open and read the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    
    #The total number of votes cast AKA the number of rows
    for row in csvreader:
        Count = Count + 1

    #A complete list of candidates who received votes
        Candidates = row[2]
        
        if row[1] not in Candidates: 
            Candidates.append(x) 
        Candidate_Votes.append(row[2])


for Candidate in Candidates:
    Votes_Per_Candidate.append(Candidate_Votes.count(Candidate))

# max_votes = max(Votes_Per_Candidate)
# winner_index = Votes_Per_Candidate.index(max_votes)
# Winner = Candidates[winner_index]
Winner = Candidate[Votes_Per_Candidate.index(max(Votes_Per_Candidate))]

print("Election Results")
print("-------------------------------")
print(f"Total Votes: {Count}")
for x in range(len(Candidates)):
    print(f"{Candidates[x]}: {Votes_Per_Candidate[x]/Count}% ({Votes_Per_Candidate[x]})")
print("-------------------------------")
print(f"Winner: {Winner}")

output = (
   f"Election Results\n"
   f"--------------------------------\n"
   ff"Total Votes: {Count}"
   f"Total: ${total_net}\n"
   f"Average  Change: ${average_month_change}\n"
   f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
   f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

with open("analysis.txt", 'w') as txt_file:
    txt_file.write(output)

    