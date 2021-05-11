# The data we need to retrieve.
#     1. The total number of votes cast
#     2. A complete list of candidates who received votes
#     3. The percentage of votes each candidate won
#     4. The total number of votes each candidate won
#     5. The winner of the elecetion based on popular vote.
# import csv
# dir(csv)

# # Assign a variable for the file to load and the path.
# file_to_load = 'Resources/election_results.csv'
# # Open the election results and read the file.
# with open(file_to_load) as election_data:

#     # To do: perform analysis.
#     print(election_data)
# import os
# print(dir(os))
# import os
# import csv
# # Assign a variable for the file to load and the path.
# file_to_load = os.path.join("Resources", "election_results.csv")
# # Open the election results and read the file.
# with open(file_to_load) as election_data:
#     # Print the file object.
#      print(election_data)

# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")
# # Using the open() function with the "w" mode we will write data to the file.
# open(file_to_save, "w")
# # Using the with statement open the file as a text file.

# outfile = open(file_to_save, "w")
# # Write some data to the file.
# outfile.write("Hello World")
# # Close the file
# outfile.close()

# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")
# # Using the with statement open the file as a text file.
# with open(file_to_save, "w") as txt_file:
#     # #write three counties to file.
#     txt_file.write("Counties in the Election\n---------\nArapahoe\nDenver\nJefferson\n")

#Add our dependencies.
import csv
import os

#Assign a variable to load a file from path.
file_to_load = os.path.join("Resources", "election_results.csv")
#Assign a variable to save a file to a path.
file_to_save = os.path.join("analysis","election_analysis.txt")

#1.Initialize a total vote counter.
total_votes=0

#Declare a list of the candidates
candidate_options = []
#Declare a dictionary for candidate votes
candidate_votes = {}

#Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    #Read and print the header row.
    headers = next(file_reader)
    # print(headers)

#Print each row in the CSV file.
    for row in file_reader:
         #2. Add to the total votes.
        total_votes += 1
        #Print the candidate name from each row
        candidate_name = row[2]
        #If the candidate does not match any existing candidate, then:
        if candidate_name not in candidate_options:
            #Add the candidate name to the candidate list.
             candidate_options.append(candidate_name)
             #Count the votes for each candidate
             candidate_votes[candidate_name] = 0
        #Increment the vote by 1 each time candidate name appears
        candidate_votes[candidate_name]+=1
#Determine the percentage of votes for each candidate
#1.Iterate through the candidate list.
for candidate_name in candidate_votes:
    #Get the vote count of a candidate.
    votes = candidate_votes[candidate_name]
    #calculate the % of votes.
    vote_percentage=float(votes)/float(total_votes)*100
    #print the candidate name and percentage of votes.
    print(f"{candidate_name} received {vote_percentage:.1f}% of the vote")

#.3. Print the number of candidate votes.
# print(candidate_votes)



