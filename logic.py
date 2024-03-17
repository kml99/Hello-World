# Program with a logic error. (Task 09) Practical Task 2
# written by K.M.Lambert
# December 2023

# program asking for input from a user asking for two numbers
# assign the two numbers to variables
# calculate the average
# display the calculated average

# ask user for two numbers and assign to variables

number_one = float(input("Enter a number: "))
number_two = float(input("\nEnter a number: "))

# calculate the average of the two numbers
number_avg = number_one + number_two / 2

# display the average number calculated
print("\nThe average of the two numbers you have entered is: ", number_avg)