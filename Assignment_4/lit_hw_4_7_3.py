"""
Tianyi Li
Class: CS 521 - Summer 2
Date: 3 August 2021
Homework Problem # 3
Description of Problem : Assign a sentence with at least 15 characters into \
a string variable, & write 2 print statements with appropriate descriptions.
"""

#Assign a sentence
sentence  = "WHO WHAT WHEN WHERE WHY"
print ("The string being analyzed is:", '"{}"'.format(sentence))

#Remove white space
sentence = sentence.split()

#Set a dictionary.
dict = {}

for i in sentence:
	if i in dict:
		dict[i] += 1
	else:
		dict[i] = 1

#Calculate result 
temp = [[k, v] for (k, v) in dict.items() if v == max(dict.values())]
result = []
for i in temp:
	result.append(i[0])

#Print result 
print("Dictionary of letter counts", dict)
print("Most frequent letter", result, "appears",temp[0][1],"times.")