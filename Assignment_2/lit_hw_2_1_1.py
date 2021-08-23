"""
Tianyi Li
Class: CS 521 - Summer 2
Date: 20 July 2021
Homework Problem # 1
Description of Problem : Prompt the user to input a number & calculate value with a formula.
"""

#Prompt the user for input.
input_number = input ("Please enter a number: ")

#Determine if the user entered a numeric value.
if input_number.isnumeric():
    number = int (input_number)
else:
    print("Wrong input; please re-enter a number: ")

#Calculate value with a formula.   
calculated_value = ((((number + 2) * 3) - 6) / 3)

#Verify and print the result.
if number == calculated_value:
    print ("The input number matches the calculated value.")
else:
    print ("The input number does not match the calculated value.")
