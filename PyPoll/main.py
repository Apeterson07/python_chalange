# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast
charles_percentage = 0
charles_votes = 0
diana_percentage = 0
diana_votes = 0
raymon_percentage = 0
raymon_votes = 0
winner = 0


# Define lists and dictionaries to track candidate names and vote counts
candidate_list = []
candidate_votes = {}

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        candidate = row[2]

        # If the candidate is not already in the candidate list, add them and increase their vote
        if candidate_list.count(candidate) == 0:
            candidate_list.append(candidate)
            candidate_votes[candidate] = 1
        else:
            candidate_votes[candidate] += 1


print('list', candidate_list)
print('votes', candidate_votes)

# Print the output
print('Election Results \n--------------------')
print("Total Votes:", total_votes)
print('--------------------')
for candidate,votes in candidate_votes.items():
    print(f'{candidate}: {round((votes/total_votes)*100,3)}% ({votes})')
print('--------------------')
print("Winner:", max(candidate_votes, key=candidate_votes.get))
print('--------------------')

output = f"""
Election Results
----------------------------
Total Votes: {total_votes}
----------------------------
"""

for candidate,votes in candidate_votes.items():
    candidate_output = f"""{candidate}: {round((votes/total_votes)*100,3)}% ({votes})\n"""
    output += candidate_output


winner_output = f"""----------------------------
Winner: {max(candidate_votes, key=candidate_votes.get)}
----------------------------
"""

output += winner_output

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)