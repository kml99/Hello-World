# This is a program written to correct a sentence (Task 02)
# written by K.M.Lambert
# December 2023
#
# set up the variable containing the sentence "The!quick!brown!fox!jumps!over!the!lazy!dog!"
# correct the sentence by removing the !
# display the corrected sentence in uppercase
# display the correct sentence in reverse

# setup of variable which includes the sentence

sentence_one = "The!quick!brown!fox!jumps!over!the!lazy!dog!"

# replace ! within the sentence and prints it

sentence_one = sentence_one.replace("!", " ")
print(sentence_one.replace("!", " "))
print()

# showing the corrected sentence in upper case
sentence_one = sentence_one.upper()
print(sentence_one)
print()

# showing the corrected sentence in upper case reveresed
print(sentence_one[ : :-1])