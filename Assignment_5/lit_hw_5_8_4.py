"""
Tianyi Li
Class: CS 521 - Summer 2
Date: 10 August 2021
Homework Problem # 4
Description of Problem : Prompt for a file name of text words.\
Words can be on many lines with multiple words per line.
""" 
import string

# The text file must be in the same file path as the main program.
def list_to_once_words(lst):
    """
    This function will return the words that appear twice in the list.

    :param list:
    :return new_list: new list with words that appeared twice in list.
    """
    new_list = []

    for char in list:
        if list.count(char) == 2 and char not in new_list:
            new_list.append(char)
    return new_list

file_name = input("Please enter the file name: ")

try:
    f1 = open(file_name, 'r')
    text = f1.read().strip()
    new_content = ''.join([i for i in text if i not in string.punctuation])
    f1.close()
    
    list = new_content.split()
    result = list_to_once_words(list)

    print(result,"These words appeared twice in the file.")

except FileNotFoundError as e:
    print(e)
