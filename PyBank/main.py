# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Define variables to track the financial data
total_months = 0
total = 0
current_month_profit = 0
previous_month_profit = 0
greatest_increase_profit = 0
greatest_decrease_profit = 0
greatest_increase_month = ''
greatest_decrease_month = ''
month_change = 0

# Add more variables to track other necessary financial data
total_month_change = 0

# Open and read the csv
with open(file_to_load) as budget_data_csv:
    reader = csv.reader(budget_data_csv)

    # Skip the header row
    header = next(reader) 

    # Process each row of data
    for row in reader:

        # Get the current month's profit
        current_month_profit = int(row[1])

        # Track the total months
        total_months = total_months + 1

        # Track the total profit/loss
        total += int(row[1])

        # Handle the first month's change
        if(total_months == 1):
            total_change = 0
            previous_month_profit = current_month_profit
            greatest_decrease_profit = 0
            greatest_increase_profit = 0
        # Handle every other month's information
        else:
            # Get the change from the previous month to the current month
            monthly_change = current_month_profit - previous_month_profit

            # Track the combined total change
            total_change += monthly_change

            # Update the previous month's infomration for the next iteration
            previous_month_profit = current_month_profit

            # Keep track of the largest increases and decreases by comparing the current change to the tracking variables
            if(monthly_change > greatest_increase_profit):
                greatest_increase_profit = monthly_change
                greatest_increase_month = row[0]
            if(monthly_change < greatest_decrease_profit):
                greatest_decrease_profit = monthly_change
                greatest_decrease_month = row[0]


# Print the output
print('Financial Analysis \n--------------------')
print("Total Months:", total_months)
print('Total: $', total, sep= '')
print('Average Change: $', round(total_change/(total_months-1),2), sep='')
print(f'Greatest Increase in Profits: {greatest_increase_month} $({greatest_increase_profit})')
print(f'Greatest Decrease in Profits: {greatest_decrease_month} $({greatest_decrease_profit})')

output = f"""
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${total}
Average Change: ${round(total_change/(total_months-1),2)}
Greatest Increase in Profits: {greatest_increase_month} $({greatest_increase_profit})
Greatest Decrease in Profits: {greatest_decrease_month} $({greatest_decrease_profit})
"""

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
