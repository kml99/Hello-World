# Award program - what prize will people receive. (Task 04) Practical Task 1
# written by K.M.Lambert
# December 2023

# Setup variables for athletes first name and last name
# Change the first letter of first namd and last name to be a Capital
# Setup variables fpr swimming, cycling and running times
# Ask user for the swimming, cycling and running times
# Display athlete's name and times for swimming, cycling and running
# change swimming, cycling and running variables to integers
# create total time for triathlon by adding swimming, cycling and running time together
# Display total time for triathlon
# display award that was awarded

# Setup of variables for atheletes name and asking for user input
athlete_firstname = input("What is your First name?  ")
athlete_lastname = input("What is your Surname? ")

# change first letter of first name and surname to a capital 
athlete_firstname_change = athlete_firstname.capitalize()
athlete_lastname_change = athlete_lastname.capitalize()

# create a variable for the full name, first name and surname
athlete_fullname = athlete_firstname_change + " " + athlete_lastname_change

# setup of variables for swimming, cycling and running times and ask for user input
swimming_time = input("What is "+ athlete_fullname + "'s swimming time, in minutes: ")
cycling_time = input("What is "+ athlete_fullname + "'s cycling time, in minutes: ")
running_time = input("What is "+ athlete_fullname + "'s running time, in minutes: ")

# Display the swimming, cycling and running times with atheletes name
print()
print(athlete_fullname, "swimming time is:  ", swimming_time)
print(athlete_fullname, "cycling time is:  ", cycling_time)
print(athlete_fullname, "running time is:  ", running_time)
print()

# Change the swimming, cycling and running times to integer
swimming_time = int(swimming_time)
cycling_time = int(cycling_time)
running_time = int(running_time)

# setup variable for total time and add swimming time, cycling time and running time together 
total_time = swimming_time + cycling_time + running_time

# display the total time
print(athlete_fullname, "Total time for Triathlon is:  ", total_time)
print()

# using total time display what award will be received
# over 111 minutes no award 
if total_time >= 111:
    print("No award will be received, participation medal only" + " for " + athlete_fullname)
    print()

# between 106 and 110 minutes a provincial scroll will be awarded    
elif total_time >= 106 <= 110:
    print("Provincial scroll to be awarded" + " to " + athlete_fullname)
    print()

# between 101 and 105 provincial half colours will be awarded
elif total_time >= 101 <= 105:
    print("Provincial Half Colours to be awarded" + " to " + athlete_fullname)
    print()

# 100 minutes and less provincial colours to be awarded
else:
   print("Provincial Colours to be awarded" + " to " + athlete_fullname)
   print()