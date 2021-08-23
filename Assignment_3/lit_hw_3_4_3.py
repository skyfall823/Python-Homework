"""
Tianyi Li
Class: CS 521 - Summer 2
Date: 27 July 2021
Homework Problem # 3
Description of Problem : Count upper, lower, digit, and punctuation.
"""

#Prompt the user to enter a sentence.
SENTENCE = input ("Please enter a sentence: ")

upper = 0
lower = 0
digits = 0
punct = 0

#Iterate through characters in sentence.
for character in SENTENCE:
    if character.isupper():
        upper +=1
    if character.islower():
        lower +=1
    if character.isnumeric():
        digits +=1
    if not (character.isalnum()):
        punct +=1


print_table = [
    [
        '# Upper', '# Lower', '# Digits', '# Punct.'
    ],
    [
        '--------', '--------', '--------', '--------'
    ],
    [
        upper, lower, digits, punct
    ]
]
for row in print_table:
    print("{: ^10} {: ^10} {: ^10} {: ^10}".format(*row))