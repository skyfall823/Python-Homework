"""
Tianyi Li
Class: CS 521 - Summer 2
Date: 10 August 2021
Homework Problem # 3
Description of Problem : Prompts the user to enter four delimited numbers\
in one request.
"""

# 
while True:
    usr_input = input('Please enter 4 delimited numbers (separated by "-"): ')
    
    value = usr_input.split('-')
    
    if len(value)<4:
        print("\nYou have entered insufficient values. Please try again.\n")
    elif len(value)>4:
        print("\nYou have entered more than 4 values. Please try again.\n")
    else:
        try:
            n1 = float (value [0])
            n2 = float (value [1])
            n3 = float (value [2])
            n4 = float (value [3])

            result = (n1 * n2 + n3) / n4
            
            output = f"({n1:,}*{n2:,}+{n3:,})/{n4:,} = {result:,}"

            print("The result is:", output) 

            break
        
        except ValueError:
            print("\nAny of the numbers entered is not integer\n")
        except ZeroDivisionError:
            print("\nZero Division Error Occured\n")