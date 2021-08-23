"""
Tianyi Li
Class: CS 521 - Summer 2
Date: 3 August 2021
Homework Problem # 4
Description of Problem : Start with 2 constant lists. Use zip to create \
a dictionary and print the new dictionary.
""" 
# Set lists.
first = ['Jane', 'John', 'Jack']
last = ['Doe', 'Deer', 'Black']


# Check for equal length.
if len(last) != len(first):
    print("Error: The length of two lists are not equal.")
else:
    new_dict = dict(zip(last, first))

# Print results.
print("First Names: " + str(first))
print("Last Names: " + str(last))
print("Name Dictionary: " + str(new_dict))
