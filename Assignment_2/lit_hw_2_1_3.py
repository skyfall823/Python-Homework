"""
Tianyi Li
Class: CS 521 - Summer 2
Date: 20 July 2021
Homework Problem # 3
Description of Problem : Enter an integer, calculate value, \
replace 'n' for user input value, & print out results.
"""

#Prompt user for input.
def calc_form (n):
    return n+n*n+n*n*n+n*n*n*n

#If statement to ensure integer was inputted.    
usr_input = input ("Please enter an integer: ")
if usr_input.isnumeric() is True:
    n = int (usr_input)
else:
    print("Wrong input; please re-enter an integer: ")

#Print result.
result = calc_form (n)
if result >= 1000:
    print ("n+n*n+n*n*n+n*n*n*n =", f"{result:,}")
else:
    print ("n+n*n+n*n*n+n*n*n*n =", result)


