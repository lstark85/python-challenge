#Import budget data
import os
import csv

#Create path to csv
csvpath=os.path.join('PyBank', 'Resources','budget_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    header = next(csvreader)
    

    #Define objects
    month = []
    profit = []
    profit_change = []
    monthly_change = []

    print(f"Header: {header}")

#Months
    for row in csvreader:
        month.append(row[0])
        profit.append(row[1])
        print(len(month))

#Profit
    profit_int= map(int, profit)
    total_profit= (sum(profit_int))
    print(total_profit)

#Average Change
    i= 0
    for i in range(len(profit)-1):
        profit_loss= int(profit[i+1])- int(profit[i])
    # Append profit_loss
        profit_change.append(profit_loss)
    Total = sum(profit_change)
    #print(profit_change)
    monthly_change = Total / len(profit_change)
    monthly_change= float(str(round(monthly_change, 2)))
    print(monthly_change)
    #print(Total)
    
#Greatest Increase
    profit_increase = max(profit_change)
    print(profit_increase)
    k = profit_change.index(profit_increase)
    month_increase = month[k+1]
    
#Greatest Decrease
    profit_decrease = min(profit_change)
    print(profit_decrease)
    j = profit_change.index(profit_decrease)
    month_decrease = month[j+1]

#Output to text file
#Print Analysis to Terminal
text_file = open("PYBankFinances.txt", "wt")
text_file.write(f'Financial Analysis'+'\n')
print(f'Financial Analysis')
text_file.write(f'----------------------------'+'\n')
print(f'----------------------------')
text_file.write("Total Months: " + str(len(month))+'\n')
print("Total Months: " + str(len(month)))
text_file.write("Total: $ " + str(total_profit)+'\n')
print("Total: $ " + str(total_profit))
text_file.write("Average Change : $" + str(monthly_change)+'\n')
print("Average Change : $" + str(monthly_change))
text_file.write(f"Greatest Increase in Profits: {month_increase} (${profit_increase})"+'\n')
print(f"Greatest Increase in Profits: {month_increase} (${profit_increase})")
text_file.write(f"Greatest Decrease in Profits: {month_decrease} (${profit_decrease})"+'\n')
print(f"Greatest Decrease in Profits: {month_decrease} (${profit_decrease})")

text_file.close()