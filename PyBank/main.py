#Import modules
import os
import csv

#Path to collect data from Resources folder
budget_data = os.path.join('Resources', 'budget_data.csv')

# CSV reader specifies delimiter and variable that holds contents
with open(budget_data) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader) 

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)

