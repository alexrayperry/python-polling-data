# Call Dependencies

import os 
import csv

# Create csv file path location

csvpath = os.path.join('election_data.csv')

# Lists for holding data values

total_votes = []

candidates = []

khan = 0

li = 0

otooley = 0

correy = 0

# Create csv reader to read in csv file

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')


    # Read header columns to confirm csv reader is working

    csv_header= next(csvreader)

    print(csv_header)

    # Read through csvfile and pull columns of data

    for row in csvreader:
        
        total_votes.append(row[0])

        candidates.append(row[2])

        if row[2] == "Khan":
            khan = khan + 1
        elif row[2] == "Li":
            li = li + 1
        elif row[2] == "O'Tooley":
            otooley = otooley + 1
        else:
            correy = correy + 1


# Check total votes list for duplicates

no_duplicates = len(set(total_votes))

# Unique Candidates from List

candidate_list = set(candidates)

# Vote Percentages

k_perc = round((khan/no_duplicates*100), 2)

l_perc = round((li/no_duplicates*100), 2)

o_perc = round((otooley/no_duplicates*100), 2)

c_perc = round((correy/no_duplicates*100), 2)


print('Election Results')
print('-------------------')
print(f'Total Votes:{no_duplicates}')
print('-------------------')
print(f'Khan: {k_perc}%')
print(f'Li: {l_perc}%')
print(f'OTooley: {o_perc}%')
print(f'Correy: {c_perc}%')
print('-------------------')
print('Winner: Khan')


