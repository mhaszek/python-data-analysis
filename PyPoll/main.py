import csv
import os
from collections import Counter

#create a path for the source data file
input_path = os.path.join('Resources', 'election_data_test_set.csv')

#create a path for the results data file
output_path = os.path.join('analysis', 'analysis.txt')

#define three empty lists to store data from each column in the source file
voter_ID = []
county = []
candidate = []

#import and read source data
with open(input_path, newline='', encoding='utf8') as csvfile:
    
    reader = csv.reader(csvfile, delimiter=",")
    
    #define first row as a header becuase it doesn't contain useable data
    csv_header = next(reader)

    #add values from the three columns to the lists
    for row in reader:
        voter_ID.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

#calculate the total number of votes cast by getting the lenght of the [voter_ID] list
total_number_of_votes = len(voter_ID)

#create a complete list of candidates who received votes by making a set of the [candidate] list
candidates_list = set(candidate)
print(candidates_list)

#The total number of votes each candidate won


#The percentage of votes each candidate won

#The winner of the election based on popular vote.


#outputs
#define each line of text for Votes Analysis
line_1 = "Election Results"
line_2 = "-------------------------"
line_3 = (f'Total Votes: {total_number_of_votes}')
line_4 = "-------------------------"
line_5 = (f'Khan: {total_number_of_votes}% ({total_number_of_votes})')
line_6 = (f'Correy: {total_number_of_votes}% ({total_number_of_votes})')
line_7 = (f'Li: {total_number_of_votes}% ({total_number_of_votes})')
line_8 = ("O'Tooley: " + str(total_number_of_votes)+"% (" + str(total_number_of_votes) + ")")
line_9 = "-------------------------"
line_10 = (f'Winner: {total_number_of_votes}')
line_11 = "-------------------------"

#add all text lines to the [print_list] list
print_list = [line_1, line_2, line_3, line_4, line_5, line_6, line_7, line_8, line_9, line_10, line_11]

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