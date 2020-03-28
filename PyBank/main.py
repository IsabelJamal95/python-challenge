import os
import csv

csvpath = os.path.join('C:/Users/Isabel/Desktop/personal-data/Homework/python-challenge/03-Python/Instructions/PyBank/Resources/budget_data.csv')
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    #skips the header row
    next(csvreader)
    #initialize the the variables
    total_months = 0
    total_profit = 0
    previous= 0
    #list is always = to []
    change_list= []
    #these lists will capture two elements, the 1st being the date, second being the value
    #initialize as 0 because it will be less than the max
    max_change= ["",0]
    #initialize as 999999 because it will be less than the max
    min_change= ["",999999]


    # Read each row of data after the header
    for row in csvreader:
        #print(row)
        #add to the count of total months through each loop
        total_months= total_months + 1   
        #get the sum of profits/losses (row[1] = 2nd column; change to interger using int())
        total_profit= total_profit + int(row[1])
        #convert row[1] into an integer for calculation
        change= int(row[1]) - previous
        previous = int(row[1])
        change_list.append(change)
        if change > max_change[1]:
            max_change[0]= row[0]
            max_change[1]= change

        if change < min_change[1]:
            min_change[0]= row[0]
            min_change[1]= change

    #average of the change_list
    #sum(change_list[1:]); starts with the second value in the list
    #(len(change_list)-1); subtract 1 from total number of elements in the change list 
    total_average= sum(change_list[1:]) / (len(change_list)-1)   
    #Find maximum Change
    #maximum_change= max(change_list)
    #Find minumum Change
    #minimum_change= min(change_list)

    #once done looping through print the total months, total profit 
    # Print Results:
    print("Financial Analysis") 
    print ("----------------------------")
    print(f'Total Months: {total_months}')
    print(f'Total: ${total_profit}')
    print(f'Average Change: ${total_average}')
    print(f'Greatest Increase in Profits: {max_change[0]} (${max_change[1]})')
    print(f'Greatest Decrease in Profits: {min_change[0]} (${min_change[1]})')

