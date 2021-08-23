"""
Tianyi Li
Class: CS 521 - Summer 2
Date: 10 August 2021
Homework Problem # 1
Description of Problem: Ask a user for a text file and then count \
the number of vowels and consonants in that file.
"""
# Text file must be in the same file path as the main program.
def vc_counter(text):
    """
    Calculate count of vowels and consonants from input text file
    :param text:
    :return:
    """
    vowels = "AEIOU"
    text = text.upper()
    v_count = len([v for v in text if v.isalpha() and v in vowels])
    c_count = len([c for c in text if c.isalpha() and c not in vowels])
    return {'vowels': v_count, 'consonants': c_count}

file_name = input ("Please enter a text file: ")
f1 = open (file_name, 'r')
text = f1.read().strip()
f1.close()
new_dict = vc_counter(text)

print("Total # of vowels in the text file: {}".format(new_dict['vowels']))
print("Total # of consonants in the text file: {}".format(new_dict['consonants']))







