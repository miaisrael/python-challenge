#Import modules
import os
import csv

#Path to collect data from Resources folder
election_data= os.path.join('Resources', 'election_data.csv')

#Read in CSV file
with open(election_data, 'r') as csvfile:

    #Split data on columns, skip header
    csvreader = csv.reader(csvfile, delimiter = ',')

    header = next(csvreader)

print(csvreader)
#Define variables
