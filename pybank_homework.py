import csv
with open("/Users/joymickle/ucb/homework/Python/python-challeng/budget_data.csv", 'r') as file:
    csvreader = csv.reader(file)
    number_of_months = -1
    total_loss_and_profit = 0
    greatest_amount = None
    greatest_month = ""
    lowest_amount = None 
    lowest_month = ""
    for row in csvreader:
        #print(row)
        number_of_months = number_of_months + 1
        if (number_of_months > 1):
            total_loss_and_profit = total_loss_and_profit + int(row[1])
            if  ((greatest_amount == None) or (int(row[1]) > greatest_amount))  and (int(row[1]) > 0):
                greatest_amount = int(row[1])
                greatest_month = row[0]

            if ((lowest_amount == None) or (lowest_amount > int(row[1])) ) and (int(row[1]) < 0):
                lowest_amount = int(row[1])
                lowest_month = row[0]


print("Number of months " + str(number_of_months))
print("Loss and profit " + str(total_loss_and_profit))
print("Greatest  increase in profits " + str(greatest_amount) + " in " + greatest_month)
print("Greatest  decrease in profits " + str(lowest_amount) + " in " + lowest_month)
