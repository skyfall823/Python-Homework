"""
Tianyi Li
Class: CS 521 - Summer 2
Date: 27 July 2021
Homework Problem # 1
Description of Problem : Count odd, even, square, and cube numbers\
from 2 to 130.
"""

#Set Constants
START = 2
END = 130

#Initialize empty lists.
odd = []
even = []
square = []
cube = []

#For loop to iterate through numbers and add to list.
for num in range (START, END + 1):
    if num % 2 == 0:
        even.append(num) 
    else:
        odd.append(num)
    if round (num ** 0.5) ** 2 == num:
        square.append(num)
    if round (num ** (1/3)) ** 3 == num:
        cube.append(num)

#Print results.
print ("Checking numbers from {} to {}".format(START, END))
print ("Odds ({}): {}...{}".format(len(odd), min(odd), max(odd)))
print ("Evens ({}): {}...{}".format(len(even), min(even), max(even)))
print ("Square ({}): {}".format(len(square), square))
print ("Cube ({}): {}".format(len(cube), cube))