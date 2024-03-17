user_name = input("\nWhat is your name? ")
num_days = int(input("\nHow many days did you work this month? "))
pay_per_day = float(input("\nHow much is your pay per day? "))     
salary = num_days * pay_per_day
print("\nMy salary for the month is USD:{}".format(salary))     