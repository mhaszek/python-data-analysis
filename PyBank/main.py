import csv
import os

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
    
    #define first row as a header becuase it doesn't contain useable data
    csv_header = next(reader)

    #add values from the two columns to the lists
    for row in reader:
        date.append(row[0])
        profit_loss.append(row[1])

#calculate the total number of months included in the dataset by getting the lenght of the [data] list
total_number_of_months = len(date)

#convert all values in the [profit_loss] list from strings to integers
profit_loss = [int(item) for item in profit_loss]

#calculate net total amount of "Profit/Losses" over the entire period by adding all values in the [profit_loss] list 
net_total_amount = sum(profit_loss)

#calculate average of the changes in "Profit/Losses" over the entire period by creating a new list of differences between each value and next value
changes_list =[]
for i in range(len(profit_loss)-1):
    changes_list.append(profit_loss[i+1] - profit_loss[i])
    
average_changes = round(sum(changes_list)/len(changes_list),2)

#calculate the greatest increase in profits over the entire period by getting the max value of the [changes_list] list
greatest_increase = max(changes_list)
#find correspondig date by getting index value from the [changes_list] list for the greatest increase and adding 1 to match the next value
greatest_increase_date = date[changes_list.index(greatest_increase)+1]
    
#calculate the greatest decrease in losses over the entire period by getting the min value of the [changes_list] list
greatest_decrease = min(changes_list)
#find correspondig date by getting index value from the [changes_list] list for the greatest increase and adding 1 to match the next value
greatest_decrease_date = date[changes_list.index(greatest_decrease)+1]

#outputs
#define each line of text for Financial Analysis
line_one = "Financial Analysis"
line_two = "----------------------------"
line_three = (f'Total Months: {total_number_of_months}')
line_four = (f'Total: ${net_total_amount}')
line_five = (f'Average Change: ${average_changes}')
line_six = (f'Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})')
line_seven = (f'Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})')

#add all text lines to the [print_list] list
print_list = [line_one, line_two, line_three, line_four, line_five, line_six, line_seven]

#define print function to print all lines of text to the terminal
def print_function(list_to_print):
    for value in list_to_print:
        print(value)

#call print function
print_function(print_list)

#write and export output data to text file
with open(output_path, 'w') as txtfile:
    #write line_one to the text file
    txtfile.write(print_list[0])

    #write all other lines as new lines to the text file
    for i in range(1,len(print_list)):
        txtfile.write("\n" + print_list[i])