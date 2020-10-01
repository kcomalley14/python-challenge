# Attach modules
import os
import csv

month_count = 0
months = []
highest_increase = 0
lowest_increase = 0
profit_losses = 0
previous_month = 0
total_monthly_change = 0

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

        #Find average change between months
        monthly_increase = monthly_profit_losses - previous_month
        total_monthly_change += monthly_increase
        previous_month = int(row[1])

        #Find High and low monthly changes
        if (monthly_increase > highest_increase):
            highest_increase = monthly_increase
            increase_month = row[0]
        
        if monthly_increase < lowest_increase:
            lowest_increase = monthly_increase
            decrease_month = row[0]
    
# Average Change between months calculated
average_change = round(total_monthly_change/month_count, 2)

#Print analysis from above
print("Financial Analysis")
print("____________________________")
print(f"Total Months: {month_count}")
print(f"Total Net Earning: ${profit_losses}")
print("Average Change: $" + str(average_change))
print(f"Greatest Increase in Profits: {increase_month} (${highest_increase})")
print(f"Greatest Decrease in Profits: {decrease_month} (${lowest_increase})")

    #Export text file of data printed
budget_output = os.path.join("Resources", "budget_data.txt")
with open("budget_data.txt", 'w') as text:
    text.write("Financial Analysis\n")
    text.write("-------------------------\n")
    text.write(f"Total Months: {month_count}\n")
    text.write(f"Total Net Earning: ${profit_losses}\n")
    text.write(f"Average Change: $" + str(average_change)+'\n')
    text.write(f"Greatest Increase in Profits: {increase_month} (${highest_increase})\n")
    text.write(f"Greatest Decrease in Profits: {decrease_month} (${lowest_increase}\n")