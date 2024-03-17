# program to generate a star pattern using a for loop (Task 08) Practical Task 1
# written by K.M.Lambert
# December 2023

# using a single for loop generate a star pattern
# set up a range to generate a star going forward and then reverse
# on the for loop display the right amount of rows with the appropriate stars
# going from 1 star to 5 stars
# then going from 5 stars to 1 star

# setup a variable to assuste with counting

star_count = 5

# Setup of for loop
for star_num in range(1, 11):  
    
    # If star_num is less than or equal to star_count, print stars in increasing order
    if star_num <= star_count:
        print("*" * star_num)
    
    # If star_num is greater than star_count, print stars in decreasing order
    else:
        print("*" * (star_count * 2 - star_num))

