# Data analysis with Python
Python project for Monash Data Analytics Boot Camp

The purpose of this project was to create Python scripts to analyse various data files.

   

# PyBank

### Data

There is one key source of data used:

* [budget_data.csv](PyBank/Resources/budget_data.csv) - .csv financial dataset composed of two columns: `Date` and `Profit/Losses`

### Analysis

* Using the financial dataset calculate:

  * The total number of months included in the dataset

  * The net total amount of "Profit/Losses" over the entire period

  * The average of the changes in "Profit/Losses" over the entire period

  * The greatest increase in profits (date and amount) over the entire period

  * The greatest decrease in losses (date and amount) over the entire period

* Export a text file with the results.

* Print the analysis to the terminal:

  ```text
  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $38382578
  Average  Change: $-2315.12
  Greatest Increase in Profits: Feb-2012 ($1926159)
  Greatest Decrease in Profits: Sep-2013 ($-2196167)
  ```


# PyPoll

### Data

There is one key source of data used:

* [election_data.csv](PyPoll/Resources/election_data.csv) - .csv set of poll data composed of three columns: `Voter ID`, `County`, and `Candidate`.

### Analysis

* Using the poll data set calculate:

  * The total number of votes cast

  * A complete list of candidates who received votes

  * The percentage of votes each candidate won

  * The total number of votes each candidate won

  * The winner of the election based on popular vote.

* Export a text file with the results.

* Print the analysis to the terminal:

  ```text
  Election Results
  -------------------------
  Total Votes: 3521001
  -------------------------
  Khan: 63.000% (2218231)
  Correy: 20.000% (704200)
  Li: 14.000% (492940)
  O'Tooley: 3.000% (105630)
  -------------------------
  Winner: Khan
  -------------------------
  ```


# PyBoss

### Data

There is one key source of data used:

* [employee_data.csv](PyBoss/Resources/employee_data.csv) -.csv employee records dataset composed of five columns: `Emp ID`, `Name`, `DOB`, `SSN`, and `State`.

### Analysis

* Convert the employee data file and export as new file:

  * Split the `Name` column into separate `First Name` and `Last Name` columns

  * Re-write the `DOB` data into `MM/DD/YYYY` format

  * Re-write the `SSN` data such that the first five numbers are hidden from view

  * Re-write the `State` data as simple two-letter abbreviations

* Export a csv file with the results.


# PyParagraph

### Data

There are three key sources of data used:

* [paragraph_1.txt](PyParagraph/Resources/paragraph_1.txt) -.txt example text file

* [paragraph_2.txt](PyParagraph/Resources/paragraph_2.txt) -.txt example text file

* [test.txt](PyParagraph/Resources/test.txt) -.txt example text file

### Analysis

* Import selected text file and asses it's the complexity by calculating the following:

  * Approximate word count

  * Approximate sentence count

  * Approximate letter count (per word)

  * Average sentence length (in words)

* Export a txt file with the results:

  ```output
  Paragraph Analysis
  -----------------
  Approximate Word Count: 130
  Approximate Sentence Count: 5
  Average Letter Count: 6.4
  Average Sentence Length: 26.0
  ```


# Demo

To run the examples locally save the chosen folder and run the `main.py` Python Script File.


# Used Tools
 * Python


#

### Contact: mil.haszek@gmail.com