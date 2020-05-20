# A set of poll data called election_data.csv is given. 
# The dataset is composed of three columns: Voter ID, County, and Candidate. 
# Create a Python script that analyzes the votes and calculates each of the following:
#   The total number of votes cast
#   A complete list of candidates who received votes
#   The percentage of votes each candidate won
#   The total number of votes each candidate won
#   The winner of the election based on popular vote.

#   Import modules 
import os
import csv
from collections import Counter

#   Open the file and read it
file=os.path.join("Resources","election_data.csv")
with open (file) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    csv_header=next(csvreader)

# Initialize lists
    poll_dt={}
    Voter_ls=[]
    Candidate_Selected_ls=[]

# Create a list that contains the candidate selected for every voter 
    for row in csvreader:
        Candidate_Selected_ls.append(row[2])
    total_votes=len(Candidate_Selected_ls)
    

# Use counter collection to know the number of votes per candidate
    c=Counter(Candidate_Selected_ls)
    dict(c)
   
    Candidate_final_ls=[]
    Candidate_votes_ls=[]
    Candiate_Percentages_ls=[]

# Convert the results to lists and make calculations
    Candidate_final_ls=list(c.keys())
    Candidate_votes_ls=list(c.values())
    Candidate_Percentages_ls=[x/ total_votes for x in  Candidate_votes_ls]
    winner=max(Candidate_votes_ls)
    winner_pos=Candidate_votes_ls.index(winner)
    winner_name=Candidate_final_ls[winner_pos]    
    
# Print Results in Console
    print("Election Results")
    print("------------------------------------------------")
    print("Total Votes: "+"{:,}".format(total_votes))
    print("------------------------------------------------")
    for i in range(len(Candidate_Percentages_ls)):
        print(Candidate_final_ls[i] + ": "+str("{:.3%}".format(Candidate_Percentages_ls[i]))+ " ("+str("{:,}".format(Candidate_votes_ls[i]))+")")
    print("------------------------------------------------")
    print(f'Winner:{winner_name}')
    print("------------------------------------------------")

# Export a text file with results
results=os.path.join("Analysis","results.txt")
with open (results,'w', newline='') as csvfile:
    csvwriter=csv.writer(csvfile, delimiter=' ', escapechar=' ', quoting=csv.QUOTE_NONE)
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["------------------------------------------------"])
    csvwriter.writerow(["Total Votes: "+str("{:,}".format(total_votes))])
    csvwriter.writerow(["------------------------------------------------"])
    for i in range(len(Candidate_Percentages_ls)):
        csvwriter.writerow([Candidate_final_ls[i] + ": "+str("{:.3%}".format(Candidate_Percentages_ls[i]))+ " ("+str("{:,}".format(Candidate_votes_ls[i]))+")"])
    csvwriter.writerow(["------------------------------------------------"])
    csvwriter.writerow([f'Winner: {winner_name}'])
    csvwriter.writerow(["------------------------------------------------"])