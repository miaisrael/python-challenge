#Import modules
import os
import csv

#Path to collect data from Resources folder
election_data= os.path.join('Resources', 'election_data.csv')

#Create lists
candidates = []
votes_won = []
votes_percent = []

#Read in CSV file
with open(election_data, 'r') as csvfile:

    #Split data on columns, skip header
    csvreader = csv.reader(csvfile, delimiter = ',')

    header = next(csvreader)
    
    #Set total votes to zero before loop begins
    total_votes = 0

#For loop to add candidates to list and/or count votes 
    for row in csvreader:
        total_votes += 1
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            votes_won.append(1)
        else:
            index = candidates.index(row[2])
            votes_won[index] += 1
    
    #For loop to add to votes percent list
    for votes in votes_won:
        percent = (votes/total_votes) * 100
        percent = round(percent)
        percent= "%.2f%%" % percent
        votes_percent.append(percent)

print(candidates)
print(votes_won)
print(votes_percent)


