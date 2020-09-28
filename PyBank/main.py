# Attach modules
import os
import csv

month_count = 0
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
    budget_header = next(budget_reader)
 
    for row in budget_reader:
        month_count += 1
        months.append(row[0])
        

    print(f"Total Months: {month_count}")