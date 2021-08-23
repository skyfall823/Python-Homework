"""
Tianyi Li
Class: CS 521 - Summer 2
Date: 27 July 2021
Homework Problem # 4
Description of Problem : Prompt the user to input a 3 digits whole number\
and ensure digits are in ascending order and without duplicates.
"""
#While loop to ensure 3 digit integer input.
while True:
    number = input('Please enter a 3-digit integer: ')

#Append user input to a list.
    x_list = []  
    for e in number:
        x_list.append(e)
        
    if not number.isdigit():
        print('Error: This is not an integer. Please re-enter.')
        continue
    
    if len(x_list) != 3: 
        print('Error: You did not enter a 3-digit number.')
        continue
      
    if x_list[0] == x_list[1] or x_list[0] == x_list [2] or x_list[1] == x_list[2]:
        print('Your number contains duplication.')
        continue

    if x_list != sorted(x_list):
        print('Error: The digits are not in ascending order.')
        continue

    else:
        break

print('Number Accepted!')
