# input for workings days and pay per day
num_days = int(input("How many days did you work this month?"))
pay_per_day = float(input("How much is your pay per day?"))   

# salary calculation
salary = num_days * pay_per_day

# print out of information
print("My salary for the month is USD:{}".format(salary))     