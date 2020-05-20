# ANALYSIS OF FINANCIAL RECORDS
#   The analysis includes:
#   The total number of months included in the dataset
#   The net total amount of "Profit/Losses" over the entire period
#   The average of the changes in "Profit/Losses" over the entire period
#   The greatest increase in profits (date and amount) over the entire period
#   The greatest decrease in losses (date and amount) over the entire period
#   Export a text file with results


#   Import modules 
import os
import csv

#   Open the file and read it
file=os.path.join("Resources","budget_data.csv")
with open (file) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    csv_header=next(csvreader)

# Initialize lists
    dates=[]
    p_l=[]
    avg_list=[]

# Add dates and P&L numbers to lists
    for row in csvreader:
        dates.append(row[0])
        p_l.append(int(row[1]))

# Output number of months and total of P&L
    months=len(dates)
    total=sum(p_l)
    print(f"Total Months: {months}")
    print("Total: "+"{:,}".format(total))
    
# Calculate average of change
    avg_list.append(0)
    for i in range(len(dates)-1):
        avg_list.append(p_l[i+1]-p_l[i])
  
    avg_change= sum(avg_list)/(len(avg_list)-1)
    print("Average Change: "+ str(round(avg_change,2)))

# Find max and min average changes. Get dates when it happened
    Max_increase=max(avg_list)
    Max_pos=avg_list.index(Max_increase)
    Max_date=dates[Max_pos]
    print(f"Greatest Increase in Profits: {Max_date} (${Max_increase})")

    Min_increase=min(avg_list)
    Min_pos=avg_list.index(Min_increase)
    Min_date=dates[Min_pos]
    print(f"Greatest Decrease in Profits: {Min_date} (${Min_increase})")

# Export a text file with results
results=os.path.join("Analysis","results.txt")
with open (results,'w', newline='') as csvfile:
    csvwriter=csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["------------------------------------------------"])
    csvwriter.writerow(["Total Months: "+str(months)])
    csvwriter.writerow(["Total: $"+str(total)])
    csvwriter.writerow(["Average Change: $"+str(round(avg_change,2))])
    csvwriter.writerow(["Greatest Increase in Profits: "+Max_date+" ($"+str(Max_increase) +")"])
    csvwriter.writerow(["Greatest Decrease in Profits: "+Min_date+" ($"+str(Min_increase) +")"])
