"""
Tianyi Li
Class: CS 521 - Summer 2
Date: 27 July 2021
Homework Problem # 2
Description of Problem : Set an odd string, confirm it, and print \
in double quotes.
"""

#Set a constant with an odd length string.
STRING = "I love BU"
#If statement to confirm odd string and print result.
if len(STRING) % 2 == 0:
    print ("String's length is even")
else:
    print ('My ' + str(len(STRING)) + ' character string is: "' + STRING + '"')
    print ('The middle character is: "' + STRING[len(STRING)//2] + '"')
    print ('The 1st half of the string is: " ' + STRING[:len(STRING)//2] + '"')
    print ('The 2nd half of string is: "' + STRING[len(STRING)//2:] + '"')
