## Chaining
import csv
import os
#Assign a variable to load a file from a path
file_to_load=os.path.join("Resources/election_results.csv")
with open(file_to_load) as election_data:
    print(election_data)
#Assign a variable to save the file to a path
file_to_save=os.path.join("analysis","election_analysis.txt")
# 1. Initialize a total vote counter.
total_votes=0
candidate_options=[]
candidate_votes={}
winning_candidate=" "
winning_count=0
winning_percentage= 0
county_options=[]
county_votes={}
#some extra initial value;
winning_county=""
winning_county_counts=0
winning_county_percentage=0
with open(file_to_load) as election_data:
    file_reader=csv.reader(election_data)
    headers=next(file_reader)
    for row in file_reader:
        total_votes+=1
        candidate_name=row[2]
        county_name=row[1]
        if county_name not in county_options:
            county_options.append(county_name)
            county_votes[county_name]=0
        county_votes[county_name]+=1
        #print(county_votes)
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name]=0
        candidate_votes[candidate_name]+=1
#passing the result into the text_file, using writted mode; with open()
with open(file_to_save,"w") as text_file:
    election_results=(
    f"\nElection Results\n"
    f"------------------\n"
    f"Total Votes:{total_votes:,}\n"
    f"--------------------------\n")
    print(election_results,end="")
    text_file.write(election_results)
    ##couting the number of country and vote
    print("\nCounty Votes:")
    for county in county_votes:
        votes_county=county_votes[county]
        votes_county_percentage=float(votes_county)/float(total_votes)*100
        
        county_results = (
           
            f"{county}:{votes_county_percentage:.1f}%({votes_county:,})"
            ) 
        
        print(county_results)
        if(votes_county>winning_county_counts) and(votes_county_percentage>winning_county_percentage):
            winning_county_counts=votes_county
            winning_county_percentage=votes_county_percentage
            winning_county=county
    # Finding the winning_county which has highest amount of votes
    winning_county_summary=(
        f"------------------\n"
        f"Largest County Turnout:{winning_county}\n")
    print(winning_county_summary)
    text_file.write(winning_county_summary)
    print("------------------\n")
    ## couting the number of candidate and vote for each
    for candidate in candidate_votes:
        votes=candidate_votes[candidate]
        votes_percentage=float(votes)/float(total_votes)*100
        candidate_results = (
            f"{candidate}: {votes_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        text_file.write(candidate_results)
        if (votes>winning_count) and (votes_percentage>winning_percentage):
            winning_count=votes
            winning_percentage=votes_percentage
            winning_candidate=candidate
    
    winning_candidate_summary=(
        f"------------------\n"
        f"Winner:{winning_candidate}\n"
        f"Winning Vote Count:{winning_count:,}\n"
        f"Winning Percentage:{winning_percentage:.1f}%\n"
        f"-------------------\n")

    print(winning_candidate_summary)
    text_file.write(winning_candidate_summary)


       
    
