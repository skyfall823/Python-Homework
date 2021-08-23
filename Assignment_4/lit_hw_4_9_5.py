"""
Tianyi Li
Class: CS 521 - Summer 2
Date: 3 August 2021
Homework Problem # 5
Description of Problem : Using my_dict = {a':15, 'c':18, 'b':20} to print\
keys and values.
"""

import operator

#Initializing dictionary
my_dict = {'a':15, 'c':18, 'b':20}

#Printing dictionary
print ("Original dictionary is : " + str(my_dict))

#Get key
print ("Keys: ", end = " ")
print([(key) for key in my_dict])
#Get value
print ("Values: ", end = " ")
print([(my_dict[key]) for key in my_dict])

print ("Key value pairs: ", end = " ")

#Display key value pairs
for i in my_dict :
    print(i, end = '')
    print(':', end = '')
    print(my_dict[i], end = ' ')
print()

#Key value pairs ordered by key
print ("Key value pairs ordered by key: ", end = " ")
print('[', end = ' ')
for k in sorted (my_dict.keys()) :
     print((k, my_dict[k]), end = " ")
print(']')
print ("Key value pairs ordered by value: ", end = " ")

#Key value pairs ordered by value
my_list = sorted(my_dict.items(), key=operator.itemgetter(1))
new_dict = dict(my_list)
print(new_dict)
