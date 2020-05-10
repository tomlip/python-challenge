# main script to run PyPoll code
# written by Thomas Lippoli

# importing needed code
import os
import csv

# temporary list

# path to data
csv_path = os.path.join("..", "PyPoll", "Resources", "election_data.csv")

# read data from csv file
with open(csv_path) as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')
    csv_header = next(csv_reader)

    # vote count variables
    khan_cnt = 0
    correy_cnt = 0
    li_cnt = 0
    otooley_cnt = 0

    for row in csv_reader:
        t_str = row[2]

        # counting votes per candidate
        if t_str == "Khan":
            khan_cnt += 1
        elif t_str == "Correy":
            correy_cnt += 1
        elif t_str == "Li":
            li_cnt += 1
        elif t_str == "O'Tooley":
            otooley_cnt += 1

total_votes = khan_cnt + correy_cnt + li_cnt + otooley_cnt

# percent variables
khan_percent = (float(khan_cnt)/float(total_votes))*100
correy_percent = (float(correy_cnt)/float(total_votes))*100
li_percent = (float(li_cnt)/float(total_votes))*100
otooley_percent = (float(otooley_cnt)/float(total_votes))*100

 # select winner
winner_cnt = max(khan_cnt, correy_cnt, li_cnt, otooley_cnt)

if winner_cnt == khan_cnt:
    winner = "Khan"
elif winner_cnt == correy_cnt:
    winner = "Correy"
elif winner_cnt == li_cnt:
    winner = "Li"
elif winner_cnt == otooley_cnt:
    winner = "O'Tooley" 

# string to record and write analysis
results = f"Election Results\n-------------------------\nTotal Votes: {total_votes}\n-------------------------\nKhan: {khan_percent:.3f}% ({khan_cnt})\nCorrey: {correy_percent:.3f}% ({correy_cnt})\nLi: {li_percent:.3f}% ({li_cnt})\nO'Tooley: {otooley_percent:.3f}% ({otooley_cnt})\n-------------------------\nWinner: {winner}\n-------------------------"

print(results)

txt_path = os.path.join("..", "PyPoll", "Analysis", "analysis.txt")

analysis_file = open(txt_path, "w")
analysis_file.write(results)