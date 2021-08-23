"""
Tianyi Li
Class: CS 521 - Summer 2
Date: 20 July 2021
Homework Problem # 7
Description of Problem : Rewrite ‘for loop’ as a ‘while loop’
"""

#Rewrite for loop as while loop.
X = 10
i = 1
while i < (X + 1): 
    if X % i == 0:
        print (i)
        i += 1
    else:
        i += 1
