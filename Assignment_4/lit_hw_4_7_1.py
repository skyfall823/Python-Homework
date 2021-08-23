"""
Tianyi Li
Class: CS 521 - Summer 2
Date: 3 August 2021
Homework Problem # 1
Description of Problem: Use list comprehension to:
find the sum of the odd and even integers in list L.
"""
# Set the list.
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Calculate sum of odd and even separately.
even_sum = sum([value for value in L if value % 2 == 0])
odd_sum = sum([value for value in L if value % 2 != 0])

# Print result.
print("Evaluating the numbers in: " + range (L))
print("Even: " + str(even_sum))
print("Odd: " + str(odd_sum))