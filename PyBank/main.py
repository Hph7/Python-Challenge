#Importing the modules
import os
import csv

#Specifying the path of CSV file
PyBankCsv = os.path.join("budget_data.csv")

#Setting variables to store the data 
total_months = 0
total_profitloss = 0
value = 0
change = 0
dates = []
profitloss = []

#Opening and reading the CSV file
with open(PyBankCsv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #Reading the header row
    csv_header = next(csvreader)

    #Reading the first row
    first_row = next(csvreader)
    total_months += 1
    value = int(first_row[1])
    total_profitloss += value
        
    #Going through each row of data after the header & first row and calculating total months
    for row in csvreader:
        dates.append(row[0])
        total_months += 1
        
        # Calculate the total profit/loss across the data
        change = int(row[1])-value
        profitloss.append(change)
        value = int(row[1])
        total_profitloss = total_profitloss + int(row[1])

    #Calculating greatest increase and decrease in profits as well as average of the changes in "Profit/Losses" over the entire period
    greatest_increase = max(profitloss)
    greatest_increase_date = dates[profitloss.index(greatest_increase)]

    greatest_decrease = min(profitloss)
    greatest_decrease_date = dates[profitloss.index(greatest_decrease)]

    average_change = sum(profitloss)/len(profitloss)

#Output of the financial analysis for PyBank
Results = (
f"Financial Analysis \n"
f"---------------------\n"
f"Total Months: {str(total_months)}\n"
f"Total: ${str(total_profitloss)}\n"
f"Average Change: ${str(round(average_change,2))}\n"
f"Greatest Increase in Profits: {greatest_increase_date} (${str(greatest_increase)})\n"
f"Greatest Decrease in Profits: {greatest_decrease_date} (${str(greatest_decrease)})")
print(Results)

#Write Output in .txt file
with open("Financial_analysis.txt", "w") as txtfile:
    write = txtfile.write(Results)