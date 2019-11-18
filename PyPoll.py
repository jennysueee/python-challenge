#importing & setting up paths
import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")
output = os.path.join("Resources", "analysis.txt")

# Set variablest
total_votes = 0
candidates = []
candidate_votes = {}
winner = ""
winning_count = 0
    
# Open and read the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    
    for row in csvreader:
        total_votes = total_votes + 1
        candidate_name = row[2]

        if candidate_name not in candidates:
            candidates.append(candidate_name)
            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

with open("PyPollAnalysis.txt", 'w') as txt_file:
    txt_file.write(output)
    output = (
    f"Election Results\n"
    f"-------------------------------\n"
    f"Total Votes: {total_votes}\n")
    txt_file.write(output)
    print(output)
        
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        percentage = float(votes) / float(total_votes) * 100

        if votes > winning_count:
            winning_count = votes
            winner = candidate
        
        voteroutput = f"{candidate}: {percentage:.1f}%, {votes}\n"
        print(voteroutput)
        txt_file.write(voteroutput)

    summaryoutput = (
    f"-------------------------------\n"
    f"Winner: {winner}\n")
    print(summaryoutput)
    txt_file.write(summaryoutput)
    
    