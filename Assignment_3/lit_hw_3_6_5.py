"""
Tianyi Li
Class: CS 521 - Summer 2
Date: 27 July 2021
Homework Problem # 5
Description of Problem : Manually create a text file with \
a single sentence of 20 words and print 4 lines with 5 words.
"""

# Making a file named test.txt having 20 words
f = open('lit_hw_q_5.txt', 'w')

# 20 words sentence.
sentence = "I like to play soccer on Friday nights at the Almansor Park, and I won a champion trophy last week"

if len(sentence.split()) > 20:
    print("Error: The sentence has more than 20 words.")
    quit()

# Writing sentence to test.txt
f.write(sentence)
f.close()  

# Reading the file
try:
    f1 = open('lit_hw_q_5.txt', 'r')
except FileNotFoundError:   # Exception handling
    print('File does not Exist')
    quit()

# Opening another file in write mode
f2 = open('new_lit_hw_q_5.txt', 'w')


line = f1.read().split()

# Making each line of 5 words and writing to second file
for i in range(0, len(line), 5):
    f2.write(' '.join(line[i:i+5]))
    f2.write('\n')

# Closing both files as good practice
f1.close()
f2.close()
