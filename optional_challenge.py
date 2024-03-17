# Program containing some errors (Task 09) optional challenge
# written by K.M.Lambert
# December 2023

# write a program with a runtime error and a logical error 

# Runtime Error Example

my_list = [1, 2, 3]
value = my_list[4]  # Accessing an index that is out of range will cause a runtime error
print(value)

# Logical Error Example

my_numbers = [10, 20, 30, 40, 50]
total = sum(my_numbers)
average = total / len(my_numbers) + 1  # Logical error: adding 1 to the average incorrectly

print(average)

