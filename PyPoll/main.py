#Import modules
import os
import csv

#Path to collect data from Resources folder
election_data= os.path.join('Resources', 'election_data.csv')

#Create list
candidates = ["Khan", "Correy", "Li", "O'Tooley"]

#Define candidate variables and set votes to zero
Candidate1 = 0
Candidate2= 0
Candidate3 = 0
Candidate4 = 0

#Read in CSV file
with open(election_data, 'r') as csvfile:

    #Split data on columns, skip header
    csvreader = csv.reader(csvfile, delimiter = ',')

    header = next(csvreader)

    #Calculate total number of votes by counting rows, not including header
    total_votes = len(list(csvreader))

    #For loop
    for row in csvreader:
        if row[2] == candidates[0]:
            Candidate1= Candidate1 + 1
        elif row[2] == candidates[1]:
            Candidate2 = Candidate2 + 1
        elif row [2] == candidates[2]:
            Candidate3 = Candidate3 + 1
        else:
            Candidate4 = Candidate4 + 1

print(total_votes)
print(candidates)
