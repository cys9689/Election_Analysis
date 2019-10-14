

## Chaining
import csv
import os
#Assign a variable to load a file from a path
file_to_load=os.path.join("Resources","election_results.csv")
with open(file_to_load) as election_data:
    print(election_data)
#Assign a variable to save the file to a path
file_to_save=os.path.join("analysis","election_analysis.txt")
# 1. Initialize a total vote counter.
total_votes=0
candidate_options=[]
candidate_votes={}
with open(file_to_load) as election_data:
    file_reader=csv.reader(election_data)
    headers=next(file_reader)
    for row in file_reader:
        total_votes+=1
        candidate_name=row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name]=0
        candidate_votes[candidate_name]+=1

        winning_candidate=" "
        winning_count=0
        winning_percentage= 0
    for candidate in candidate_votes:
        votes=candidate_votes[candidate]
        votes_percentage=float(votes)/float(total_votes)*100
        if (votes>winning_count) and (votes_percentage>winning_percentage):
            winning_count=votes
            winning_percentage=votes_percentage
            winning_candidate=candidate
    winning_candidate_summary=(
        f"------------------\n"
        f"Winner:{winning_candidate}"
        f"Winning Vote Count:{winning_count:,}\n"
        f"Winning Percentage:{winning_percentage:.1f}%\n"
        f"-------------------\n")
    print(winning_candidate_summary)


       
    
