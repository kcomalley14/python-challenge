# Attach modules
import os
import csv

months = []
profit_losses = []
total_months = []

print("Financial Analysis")
print("____________________________")

# Set path for file analysis
budget_csv = os.path.join("Resources", "budget_data.csv")

# Access the CSV file
with open(budget_csv) as csvfile:
    budget_reader = csv.reader(csvfile, delimiter=",")
    #budget_header = next(csvfile)
    for row in budget_reader:

        #find number of months
        total_months = len(list(budget_reader))
        print(f"Total Months: {total_months}")

    
        