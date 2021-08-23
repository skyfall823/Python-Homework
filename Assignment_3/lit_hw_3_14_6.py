"""
Tianyi Li
Class: CS 521 - Summer 2
Date: 27 July 2021
Homework Problem # 6
Description of Problem : Create a text file containing student record.
"""

# Making a new file.
f = open('lit_hw_q_6.txt', 'w')

# Adding student data.
f.write('Tyrion Lannister, 1, 3.7')
f.write('\n')
f.write('Daenerys Targaryen, 52, 2.8')
f.write('\n')
f.write('Jon Snow, 13, 3.9')
f.write('\n')
f.write('Sansa Stark, 24, 3.4')

#Close file.
f.close()

# Reading the file
try:
    f1 = open('lit_hw_q_6.txt', 'r')
except FileNotFoundError:  # Exception handling
    print('File does not Exist')
    quit()

# Initialize list.
student_data = []

for student in f1:
    student_data.append(student.strip().split(', '))  

# Print result. 
print(student_data)

# Close file.
f1.close()
