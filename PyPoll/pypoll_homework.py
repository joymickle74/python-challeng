import csv
with open("/Users/joymickle/ucb/UCB-VIRT-DATA-PT-04-2023-U-LOLC/02-Homework/03-Python/Starter_Code/PyPoll/Resources/election_data.csv", 'r') as file:
    csvreader = csv.reader(file)
    number_of_votes = -1
    candidates = {}
    for row in csvreader:
        number_of_votes = number_of_votes +1
        if (number_of_votes > 0):
            candidate = row[2]
            if candidate in candidates:
                candidates[candidate] = candidates[candidate] + 1 
            else:
                candidates[candidate] = 1
    print("Total number of votes "+ str(number_of_votes))
    for candidate in candidates:
        print("Vote for " + candidate + ": " + str(candidates[candidate]))