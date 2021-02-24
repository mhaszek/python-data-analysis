import csv
import os

#create a path for the source data file
input_path = os.path.join('Resources', 'election_data.csv')

#create a path for the results data file
output_path = os.path.join('analysis', 'analysis.txt')

#define two empty lists to store data from relevant columns in the source file
voter_ID = []
candidate = []

#import and read source data
with open(input_path, newline='', encoding='utf8') as csvfile:
    
    reader = csv.reader(csvfile, delimiter=",")
    
    #define first row as a header becuase it doesn't contain useable data
    csv_header = next(reader)

    #add values from the two columns to the lists
    for row in reader:
        voter_ID.append(row[0])
        candidate.append(row[2])

#calculate the total number of votes cast by getting the lenght of the [voter_ID] list
total_number_of_votes = len(voter_ID)

#create a complete list of candidates who received votes by making a set of the [candidate] list
candidates_list = set(candidate)

#initialize a dictionary with default values equal to zero
votes_count = {}.fromkeys(candidates_list, 0)

#loop through the [candidate] list and count each vote to get the total number of votes each candidate won
for person in candidate:
    votes_count[person] += 1

#initialize a dictionary with default values equal to zero
votes_percentage = {}.fromkeys(candidates_list, 0)

#loop through the [candidates_list] list and calculate percentage of votes each candidate won
for person in candidates_list:
    votes_percentage[person] = votes_count[person]/total_number_of_votes

#find the winner of the election based on popular vote using max function 
winner = max(votes_count, key=votes_count.get)

#outputs
#define each line of text for Votes Analysis
line_1 = "Election Results"
line_2 = "-------------------------"
line_3 = (f'Total Votes: {total_number_of_votes}')
line_4 = ("Khan: " +"{:.3%}".format(votes_percentage["Khan"])+" (" + str(votes_count["Khan"]) + ")")
line_5 = ("Correy: " +"{:.3%}".format(votes_percentage["Correy"])+" (" + str(votes_count["Correy"]) + ")")
line_6 = ("Li: " +"{:.3%}".format(votes_percentage["Li"])+" (" + str(votes_count["Li"]) + ")")
line_7 = ("O'Tooley: " +"{:.3%}".format(votes_percentage["O'Tooley"])+" (" + str(votes_count["O'Tooley"]) + ")")
line_8 = (f'Winner: {winner}')

#add all text lines to the [print_list] list
print_list = [line_1, line_2, line_3, line_2, line_4, line_5, line_6, line_7, line_2, line_8, line_2]

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