# This is a program written to manipulate a sentence (Task 02)
# written by K.M.Lambert
# December 2023
# Request that the user enter a sentence which will be stored as a variable in str_manip
# Calculate the length of the inputted string and display this to the user
# Find the last letter of the inputted string and replace every occurance within the string with @
# Display the last 3 characters of the string backwards
# Create five letter word which is created by using the first three characters and last two characters from the variable str_manip

# requesting a sentence from user
str_manip = input("Please enter a sentence: ")

# determine the length of the string
print(len(str_manip))

# determine what is the last letter in the string and assign to a new variable
str_manip_end = str_manip[-1: : ]

# print(str_manip[-1: :])  used for testing to ensure last letter was found
print(str_manip_end)

# replace the letter that was found in previous step with the @ sign
str_manip_replace = str_manip.replace(str_manip_end, "@")
print(str_manip_replace)

# locate the last three characters, assign to a new variable and print them backwards
str_manip_three = str_manip[-3: ]
print(str_manip_three)
print(str_manip_three[ : :-1])

# display the first three characters and last two characters from the string inputted by user
# print(str_manip[0:3],str_manip[-2:])  Tried it this way first but it left a space between
first_three = str_manip[0:3]
last_two = str_manip[-2:]
print(first_three+last_two)