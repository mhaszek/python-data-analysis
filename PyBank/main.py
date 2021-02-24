import csv
import os
import string

#create a path for the source data file
input_path = os.path.join('Resources', 'budget_data.csv')

#create a path for the results data file
output_path = os.path.join('analysis', 'analysis.txt')

#define two empty lists to store data from each column in the source file
date = []
profit_loss = []

#import and read source data
with open(input_path, newline='', encoding='utf8') as csvfile:
    
    reader = csv.reader(csvfile, delimiter=",")
    
    #define first row as a header becuase it doesn't contain usable data
    csv_header = next(reader)

#    print("HEADER: " + str(csv_header))

    #add values from the two columns to the lists
    for row in reader:
        date.append(row[0])
        profit_loss.append(row[1])

    #calculate the total number of months included in the dataset by getting the lenght of the [data] list
    total_number_of_months = len(date)
    print(total_number_of_months)

    #convert all values in the [profit_loss] list from strings to integers
    profit_loss = [int(item) for item in profit_loss]

    #calculate net total amount of "Profit/Losses" over the entire period by adding all values in the [profit_loss] list 
    net_total_amount = sum(profit_loss)
    print(net_total_amount)

    #calculate average of the changes in "Profit/Losses" over the entire period by creating a new list of differences between each value and next value
    changes_list =[]
    for i in range(len(profit_loss)-1):
        changes_list.append(profit_loss[i+1] - profit_loss[i])
    
    average_changes = round(sum(changes_list)/len(changes_list),2)
    print(average_changes)

    #calculate the greatest increase in profits over the entire period by getting the max value of the [changes_list] list
    greatest_increase = max(changes_list)
    print(greatest_increase)
    #find correspondig date by getting index value from the [changes_list] list for the greatest increase and adding 1 to match the next value
    print(date[changes_list.index(greatest_increase)+1])
    
    #calculate the greatest decrease in losses over the entire period by getting the min value of the [changes_list] list
    greatest_decrease = min(changes_list)
    print(greatest_decrease)
    #find correspondig date by getting index value from the [changes_list] list for the greatest increase and adding 1 to match the next value
    print(date[changes_list.index(greatest_decrease)+1])

