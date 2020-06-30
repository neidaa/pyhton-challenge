#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Dependencies 
import csv


# In[ ]:


# Files to load and output 
file_to_load = "raw_data/election_data_1.csv"
file_to_output = "analysis/election_analysis_1.txt"

# Total Vote Counter 
total_votes = 0 


# In[ ]:


# Candidate options and vote counters 
candidate_options = []
candidate_votes = {}


# In[ ]:


# Winning candidates and winning count tracker
winning_candidate = ""
winning_count = 0


# In[ ]:


# Read in the csv and convert it into a list of dictionaries 
with open(file_to_load) as election_data:
    reader = csv.DictReader(election_data)
    
    
    # For each row
    for row in reader:
        
        # Add to the total vote count 
        total_votes = total_votes + 1
        
        # Extract the candidate name from each row
        candidate_name = row["Candidate"]
        
        # If the candidate does not match any exisiting candidate 
        if candidate_name not in candidate_options:
            
            # Add it to the list of candidates in the running
            candidate_options.append(candidate_name)
            
            # And begin tracking that candidates voter count 
            candidate_votes[canidate_name] = 0
        
        # Then add a vote to that candidate's count 
        candidate_votes[candidates_name] = candidate_votes[candidate_name] + 1


# In[ ]:


# Print the results and export the data to the text file 
with open (file_to_ouput, "w") as txt_file:
    
    # Print the finalvote count 
    election_results = (
    f"\n\nElection Results\n"
    f"---------------------\n"
    f"Total Votes: {total_votes}\n"
    f"--------------------------\n"
        
    )
    print(election_results)

