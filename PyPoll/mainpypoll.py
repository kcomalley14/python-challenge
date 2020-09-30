import os
import csv

total_votes = 0
candidate_list = []
votecount = {}
vote_percent = {}
candidate = ""
winner_votes = 0
winner = ""

# Set path for file
election_data_csv = os.path.join("Resources", "election_data.csv")

# access csv file
with open(election_data_csv) as csvfile:
    election_reader = csv.reader(csvfile, delimiter= ",")
    election_header = next(election_reader)

    # Total up votes
    for row in election_reader:
        total_votes += 1
        candidate = row[2]
        if candidate in votecount:
            votecount[candidate] += 1
        else:
            votecount[candidate] = 1
        
    # Find voter percentage and winner
    for candidate, votes in votecount.items():
        vote_percent[candidate] = "{:.1%}".format(votes / total_votes)
        if votes > winner_votes:
            winner_votes = votes
            winner = candidate

print("Election Results")
print("------------------------")
print(f"Total Votes: {total_votes}")
print("------------------------")

for candidate, votes in votecount.items():
    print(f"{candidate}: {vote_percent[candidate]} + {votes}")

print("------------------------")
print(f"Winner: {winner}")
print("------------------------") 
