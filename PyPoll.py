

## Chaining
import csv
import os

file_to_load=os.path.join("Resources","election_results.csv")
with open(file_to_load) as election_data:
    print(election_data)

file_to_save=os.path.join("analysis","election_analysis.txt")
with open(file_to_load) as election_data:
    file_reader=csv.reader(election_data)
    headers=next(file_reader)
    print(headers)
    
