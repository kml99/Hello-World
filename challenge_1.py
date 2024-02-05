# This is a program written to calculate the sides of a triangle (Task 02) optional challenge 1
# written by K.M.Lambert
# December 2023
# Ask user for input regarding the length of the sides of the triangle
# assign the input to variables and make those variables integers
# perform calculations to determine area of triangle
# Display calculated area of inputted triangle 

#import math                        Tried to use this first but couldn't get it to work, so I tried another way which did work.  Will have another go at 1st way 

# Ask user for input regarding numbers for the sides of a triangle
side_one = input("Please enter number for first side: ")
side_two = input("Please enter number for second side: ")
side_three = input("Please enter number for third side:")

# print(side_one, side_two, side_three)                 used for testing
print()

# Change variables to integer
side_one = int(side_one)
side_two = int(side_two)
side_three = int(side_three)

# Calculate the semi-perimeter /base
tri_sides = (side_one + side_two + side_three) / 2

#tri_area = math.sqrt(tri_sides(tri_sides-side_one)*(tri_sides-side_two)*(tri_sides-side_three)) ** 0.5    Part of 1st attempt will play around with it a bit more to see what I was doing wrong
# Calculate the area and display the result

tri_area = (tri_sides*(tri_sides-side_one)*(tri_sides-side_two)*(tri_sides-side_three)) ** 0.5

print ('The area of the triangle is %0.2f'  %tri_area)