#Importing the modules
import os
import csv

#Specifying the path of CSV file
file_name = os.path.join("election_data.csv")

#Setting variables
num_votes = 0
votes = []
candidates = []
percentages = []
max_index = 0

#Opening and reading the CSV file
with open(file_name) as csvfile:
    csvreader = csv.reader(csvfile)

    #Reading the header row
    line = next(csvreader,None)

    #Going through each row of data after the header
    for line in csvreader:
        num_votes = num_votes + 1
        candidate = line[2]

        if candidate in candidates:
            candidate_index = candidates.index(candidate)
            votes[candidate_index] = votes[candidate_index] + 1
        else:
            candidates.append(candidate)
            votes.append(1)
                

max_votes = votes[0]
for count in range(len(candidates)):
    vote_percentage = votes[count]/num_votes*100
    percentages.append(vote_percentage)
    if votes[count] > max_votes:
        max_votes = votes[count]
        max_index = count
winner = candidates[max_index]

#Print output of poll analysis
print("Election Results")
print("--------------------------")
print(f"Total Votes: {num_votes}")
print("--------------------------")
for count in range(len(candidates)):
    print(f"{candidates[count]}: {percentages[count]}% ({votes[count]})")
print("---------------------------")
print(f"Winner: {winner}")
print("---------------------------")

#output in txt file
with open("Election_results.txt", "w") as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("--------------------------\n")
    txtfile.write(f"Total Votes: {num_votes}\n")
    txtfile.write("--------------------------\n")
    for count in range(len(candidates)):
        txtfile.write(f"{candidates[count]}: int{percentages[count]}% ({votes[count]})\n")
    txtfile.write("---------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("---------------------------\n")
