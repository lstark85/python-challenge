#import poll
import os
import csv

#Create path to csv
csvpath=os.path.join( 'Resources','election_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    header = next(csvreader)
    
    #Define Objects
    votes = []
    county = []
    candidates = []
    khan = []
    correy = []
    li = []
    otooley = []

#Create append list
    for row in csvreader:
        votes.append(int(row[0]))
        county.append(row[1])
        candidates.append(row[2])

    #Count Votes
    total_votes = (len(votes))
    #print(total_votes)

    #Votes by Person
    for candidate in candidates:
        if candidate == "Khan":
            khan.append(candidates)
            khan_votes = len(khan)
        elif candidate == "Correy":
            correy.append(candidates)
            correy_votes = len(correy)
        elif candidate == "Li":
            li.append(candidates)
            li_votes = len(li)
        else:
            otooley.append(candidates)
            otooley_votes = len(otooley)
    #print(khan_votes)
    #print(correy_votes)
    #print(li_votes)
    #print(otooley_votes)
    
    
    #Percentages
    khan_percent = round(((khan_votes / total_votes) * 100), 2)
    correy_percent = round(((correy_votes / total_votes) * 100), 2)
    li_percent = round(((li_votes / total_votes) * 100), 2)
    otooley_percent = round(((otooley_votes / total_votes) * 100), 2)
    #print(khan_percent)
    #print(correy_percent)
    #print(li_percent)
    #print(otooley_percent)
    
    #Winner 
    if khan_percent > max(correy_percent, li_percent, otooley_percent):
        winner = "Khan"
    elif correy_percent > max(khan_percent, li_percent, otooley_percent):
        winner = "Correy"  
    elif li_percent > max(correy_percent, khan_percent, otooley_percent):
        winner = "Li"
    else:
        winner = "O'Tooley"

        #Output to text file
        #Print Statements

text_file= open("PYPoll_Results.txt", "wt")
text_file.write(f"Election Results" + "\n")
print(f"Election Results" + "\n")
text_file.write(f"-----------------------------------" + "\n")
print(f"-----------------------------------" + "\n")
text_file.write(f"Total Votes: {total_votes}" + "\n")
print(f"Total Votes: {total_votes}" + "\n")
text_file.write(f"-----------------------------------" + "\n")
print(f"-----------------------------------" + "\n")
text_file.write(f"Khan: {khan_percent}% ({khan_votes})" + "\n")
print(f"Khan: {khan_percent}% ({khan_votes})" + "\n")
text_file.write(f"Correy: {correy_percent}% ({correy_votes})" + "\n")
print(f"Correy: {correy_percent}% ({correy_votes})" + "\n")
text_file.write(f"Li: {li_percent}% ({li_votes})" + "\n")
print(f"Li: {li_percent}% ({li_votes})" + "\n")
text_file.write(f"O'Tooley: {otooley_percent}% ({otooley_votes})" + "\n")
print(f"O'Tooley: {otooley_percent}% ({otooley_votes})" + "\n")
text_file.write(f"-----------------------------------" + "\cdcdn")
print(f"-----------------------------------" + "\n")
text_file.write(f"Winner: {winner}" + "\n")
print(f"Winner: {winner}" + "\n")
text_file.write(f"-----------------------------------")
print(f"-----------------------------------")
text_file.close()
