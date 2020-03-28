import os
import csv

csvpath = os.path.join('C:/Users/Isabel/Desktop/personal-data/Homework/python-challenge/03-Python/Instructions/PyPoll/Resources/election_data.csv')
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    #skips the header row
    next(csvreader)

    #initialize variables
    total_votes = 0
    winner= ""
    winner_count= 0
    

    candidates_list= []
    candidate_dict= {}

    # Read each row of data after the header
    for row in csvreader:
        total_votes= total_votes + 1

       
        candidate= row[2]
        if candidate not in candidates_list:
            candidates_list.append(candidate)
            candidate_dict[row[2]]= 0
        candidate_dict[row[2]]= candidate_dict[row[2]] + 1
    print ("Election Results")   
    print ("-------------------------") 
    print (f'Total Votes: {total_votes}')  
    print ("-------------------------")
    #print(candidate_dict) 

    for name in candidate_dict:
        votes= candidate_dict[name]   
        percentage= round(votes/total_votes * 100)
        print(f' {name}: {percentage}% ({votes})')

        if votes > winner_count:
            winner_count= votes
            winner= name
    print("-------------------------")

    
    print(f'Winner: {winner}')

    print("-------------------------")

