#Import modules
import os
import csv

#Path to collect data from Resources folder
budget_data = os.path.join('Resources', 'budget_data.csv')

#Read in CSV file
with open(budget_data, 'r') as csvfile:

    #Split data on commas/columns
    csvreader= csv.reader(csvfile, delimiter=',')

    header= next(csvreader)

#Define variables for calculations and set at 0
    months = 0
    prof_loss = 0
    total_change = 0
    last_month = 0
    first_loop = True
    current_change = 0
    max_change = 0
    max_date = 0
    min_change = 0
    min_date = 0

#For loop for totals to count months and profit/loss
    for line in csvreader:
        months = months + 1
        prof_loss = prof_loss + int(line[1])    
        if first_loop == False:
            current_change = int(line[1]) - last_month
            total_change = total_change + current_change
        last_month = int(line[1])
        if current_change > max_change:
            max_change = current_change
            max_date = line[0]
        if current_change < min_change:
            min_change = current_change
            min_date = line[0]
        first_loop = False

#Caluclate average change   
average_change = total_change/ (months - 1)

#Print analysis
print("Financial Analysis")
print("*******************")
print("Total Months: ", months)
print("Total: ", "$", prof_loss)
print("Average Change: ", "$", round(average_change))
print("Greatest Increase in Profits: ", max_date, "(","$",max_change,")")
print("Greatest Decrease in Profits: ", min_date, "(","$",min_change,")")

#List for analysis table
categories = ["Financial Analysis", "*****************", "Total Months:", "Total:", "Average Change:", "Greatest Increase in Profits:", "Greatest Decrease in Profits:"]
stats = [" ", " ", months, prof_loss, average_change, max_date, min_date]
stats_2= [" ", " ", " ", " ", " ", max_change, min_change]


analysis_table= zip(categories, stats, stats_2)

#Write analysis to text file, set variable for new output file
output_file = os.path.join('Analysis', "Financial Analysis.txt")

#Open the output file
with open(output_file, "w") as textfile:
    writer = csv.writer(textfile)

    writer.writerows(analysis_table)