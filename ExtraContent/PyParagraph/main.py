import os
import string
import re

#create a path for the source data file
input_path = os.path.join('Resources', 'paragraph_1.txt')

#create a path for the results data file
output_path = os.path.join('output', 'analysis.txt')

#import and read source data
with open(input_path, 'r') as txtfile:
    
    reader = txtfile.read()

    #calculate approximate word count by adding splitting the text into a list and getting the list's length
    words = reader.split()
    words_count = len(words)

    #calculate approximate sentence count by splitting the text by "(?<=[.!?]) +" characterts into a list and getting the list's length
    sentences = re.split("(?<=[.!?]) +", reader)
    sentences_count = len(sentences)

    #calculate average letter count by getting the string length for each item in the list [words], adding them together, then dividing by all words
    letters = 0
    for word in words:
        letters = letters + len(word)
    letters_count = round(letters/words_count,1)

    #calculate average sentence length dividing words_count by sentences_count
    sentence_length = round(words_count/sentences_count,1)

#outputs
#define each line of text for Votes Analysis
line_1 = "Paragraph Analysis"
line_2 = "-----------------"
line_3 = (f'Approximate Word Count: {words_count}')
line_4 = (f'Approximate Sentence Count: {sentences_count}')
line_5 = (f'Average Letter Count: {letters_count}')
line_6 = (f'Average Sentence Length: {sentence_length}')

#add all text lines to the [print_list] list
print_list = [line_1, line_2, line_3, line_4, line_5, line_6]

#define print function to print all lines of text to the terminal
def print_function(list_to_print):
    for value in list_to_print:
        print(value)

#call print function
print_function(print_list)

#write and export output data to text file
with open(output_path, 'w') as txtfile:
    #write line_1 to the text file
    txtfile.write(print_list[0])

    #write all other lines as new lines to the text file
    for i in range(1,len(print_list)):
        txtfile.write("\n" + print_list[i])