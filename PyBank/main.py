# Attach modules
import os
import csv

month_count = 0
months = []
profit_losses = 0

print("Financial Analysis")
print("____________________________")

# Set path for file analysis
budget_csv = os.path.join("Resources", "budget_data.csv")

# Access the CSV file
with open(budget_csv) as csvfile:
    budget_reader = csv.reader(csvfile, delimiter=",")
    budget_header = next(budget_reader)
    # loop through rows of budget_reader
    for row in budget_reader:
        #find total months
        month_count += 1
        months.append(row[0])
        # find net amount profits over period
        monthly_profit_losses = int(row[1])
        profit_losses += monthly_profit_losses



    print(f"Total Months: {month_count}")
    print(f"Total Net Earning: {profit_losses}")