# main script to run PyBank Analysis code
# written by Thomas Lippoli

# importing needed code
import os
import csv

# temporary list

# path to data
csv_path = os.path.join("..", "PyBank", "Resources", "budget_data.csv")

# read data from csv file
with open(csv_path) as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')
    csv_header = next(csv_reader)
    bank_list = list()
    cnt = 0
    net_sum = 0.0
    max_profit = 0.0
    max_loss = 0.0

    for row in csv_reader:
        cnt += 1
        t_month = row[0]
        num = float(row[1])
        net_sum += num
        # rewrite max profit/loss variables and assign months to them as needed
        if num > max_profit:
            max_profit = num
            profit_month = t_month
        
        if num < max_loss:
            max_loss = num
            loss_month = t_month

mean_change = net_sum/cnt

# string to record and write analysis
results = f"Financial Analysis\n----------------------------\nTotal Months: {cnt}\nTotal: ${int(net_sum)}\nAverage Change: ${mean_change:.2f}\nGreatest Increase in Profits: {profit_month} (${int(max_profit)})\nGreatest Decrease in Profits: {loss_month} (${int(max_loss)})"

print(results)

txt_path = os.path.join("..", "PyBank", "Analysis", "analysis.txt")

analysis_file = open(txt_path, "w")
analysis_file.write(results)