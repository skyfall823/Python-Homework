"""
Tianyi Li
Class: CS 521 - Summer 2
Date: 3 August 2021
Homework Problem # 2
Description of Problem : Generate a new list with each \
integer in the new list is the sum of its nearest neighbor.
"""

# Set list.
list=[10, 20, 30, 40, 50]

# Perform calculation.
result=[]
for i in range(len(list)):
    #for first element
    if i==0:
        result.append(list[i]+list[i+1])
    
    #for last element.
    elif i==len(list)-1:
        result.append(list[i]+list[i-1])

    #for all other elements.
    else:
        result.append(list[i]+list[i-1]+list[i+1])

# Print original and result list.
print("Input List:", list)
print("Result List:", result)