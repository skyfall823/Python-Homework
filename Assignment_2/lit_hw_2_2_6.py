"""
Tianyi Li
Class: CS 521 - Summer 2
Date: 20 July 2021
Homework Problem # 6
Description of Problem : Calculate leap year.
"""

#For Loop
for year in range (1899, 2021):
    if year % 4 == 0 and year % 100 != 0:
        print (year, end=",")
        
print (" ") # Line Break

#While Loop
year_int = 1899
while year_int <= 2021:
    if (year_int % 4 == 0) and (year_int % 100 != 0):
        print (year_int, end=",")
        year_int += 1
    else:
        year_int += 1 




