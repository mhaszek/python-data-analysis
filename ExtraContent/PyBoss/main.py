import os
import csv
import datetime

#create a path for the source data file
input_path = os.path.join('Resources', 'employee_data.csv')

#take the filename from the original path
_, filename = os.path.split(input_path)

#create a path for the results data file with the same name as the source data file
output_path = os.path.join('output', filename)

#define empty lists to store data from the columns in the source file
emp_id = []
first_name = []
last_name = []
dob = []
ssn = []
state = []

#add dictionary which contains US state abbreviations from 'afhaque' github
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

#import and read source data
with open(input_path, 'r', newline='', encoding='utf8') as file:

    reader = csv.reader(file, delimiter=',')
    
    #define first row as a header becuase it doesn't contain useable data 
    csv_header = next(reader)

    #go through each row in the source data and write required outputs into new lists
    for row in reader:
        
        #write unchanged Employee ID number into [emp_id] list
        emp_id.append(row[0])
        
        #split [name] column into [first_name] and [last_name] lists
        name = row[1].split(" ")
        first_name.append(name[0])
        last_name.append(name[1])
        
        #re-write [DOB] column into MM/DD/YYYY format
        date_obj = datetime.datetime.strptime(row[2], "%Y-%m-%d")
        formated_date = datetime.date.strftime(date_obj, "%m/%d/%Y")
        dob.append(formated_date)
        
        #re-write [SSN] column with the first five numbers hidden
        org_ssn = row[3].split("-")
        ssn.append("***-**-" + org_ssn[2])
        
        #re-write [state] column as two-letter abbreviations
        state.append(us_state_abbrev[row[4]])

#zip all new lists together        
new_file = zip(emp_id, first_name, last_name, dob, ssn, state)

#write and export output data to a new file
with open(output_path, 'w', newline='') as file:
    
    csvwriter = csv.writer(file)

    #write headers for the first line
    csvwriter.writerow(["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"])
    
    #write the rest of the lines with zipped new lists
    csvwriter.writerows(new_file)