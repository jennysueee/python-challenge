#importing & setting up paths
import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")
output = os.path.join("Resources", "analysis.txt")

# I know I didn't get this right but ran out of time to troubleshoot. 

# Set variables
Candidates = {}
Count = 0
Number_of_Votes = 0
Percent_of_votes = 0
Most_Votes = 0
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

        if candidate in Candidates:
            candidate_index = Candidates.index(candidate)
            Number_of_Votes[candidate_index] = Count[candidate_index] + 1

        else:
            Candidates.append(candidate)
            number_of_votes.append(1)


print("Election Results")
print("-------------------------------")
print(f"Total Votes: {Count}")
for count in range(len(Candidates)):
    print(f"{Candidates[count]}: {Percent_of_votes[count]}% ({Number_of_Votes[count]})")
print("-------------------------------")
print(f"Winner: {Winner}")

output = (
   f"Financial Analysis\n"
   f"--------------------------------\n"
   f"Total Months: {total_months}\n"
   f"Total: ${total_net}\n"
   f"Average  Change: ${average_month_change}\n"
   f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
   f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

with open("analysis.txt", 'w') as txt_file:
    txt_file.write(output)

    