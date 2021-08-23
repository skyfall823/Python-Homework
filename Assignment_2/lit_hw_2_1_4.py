"""
Tianyi Li
Class: CS 521 - Summer 2
Date: 20 July 2021
Homework Problem # 4
Description of Problem : 3 line program to prompt a number, \
convert to an integer, & print 0 for even number and 1 for odd.
"""

#Finish the code in 3 lines.
usr_input = input ("Please enter a number: ")
number = int (usr_input)
print (0 if number % 2 == 0 else 1)

