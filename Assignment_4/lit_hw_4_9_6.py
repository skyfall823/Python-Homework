"""
Tianyi Li
Class: CS 521 - Summer 2
Date: 3 August 2021
Homework Problem # 6
Description of Problem : Create a program that prompt for input, validate\
the number, convert it to word with dictionary, and print out as words.
"""
# Set a dictionary.
dict = {"1": "One","2": "Two","3": "Three","4": "Four",
        "5": "Five","6": "Six","7": "Seven","8": "Eight",
        "9": "Nine", "0": "Zero",".": "Point", "-": "Negative"}

# Infinite while loop
while True:
    if_valid = 1

    number = input("Enter a number: ")

    as_text = " "

    for char in number:
        if char in dict.keys():
            as_text += dict[char] + " "
        elif char == ",":
            print("Please try again without entering commas.")
            if_valid = 0
            break
        else:
            print(f"{number} is not a valid number. Please try again")
            if_valid = 0
            break
        
    if if_valid == 0:
        continue
    else:
        print(f"As Text: {as_text}")
        break
