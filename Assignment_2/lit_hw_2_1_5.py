"""
Tianyi Li
Class: CS 521 - Summer 2
Date: 20 July 2021
Homework Problem # 5
Description of Problem : Calculate Body Mass Index (BMI).
"""

#Prompt for height and weight in one input.
height, weight = input ("Please enter your height in meters \
and weight in kilograms separated by space: ").split()

#Calculation formula.
bmi = float (weight) / (float (height) ** 2)

#Print result.
print ("Body Mass Index (BMI) for Height", height, "and", \
"Weight", weight, ":", bmi)
