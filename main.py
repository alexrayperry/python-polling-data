# Call Dependencies

import os 
import csv

# Create csv file path location

csv_path = os.path.join('election_data.csv')

# Lists for holding data values

total_votes = []

# Create csv reader to read in csv file

with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read over header columns

    csv_header= next(csvreader)

    # Read through csvfile and pull columns of data

    for row in csvreader:
        
        total_votes.append(row[0])


print(len(total_votes))

