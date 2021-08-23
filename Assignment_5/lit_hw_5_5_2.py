"""
Tianyi Li
Class: CS 521 - Summer 2
Date: 10 August 2021
Homework Problem # 2
Description of Problem : Create 3 functions with docstring: letter_counts(),\
most_common_letter(), string_count_histogram()
"""

# Define Function
def letter_counts(str1):
  """ Function to return dictionary with keys as character and values as their frequency"""
  dict_1 = {}

  for char in str1:  
    if char != ' ':  
      if char in dict_1:  
        dict_1[char] += 1
      else:          
        dict_1[char] = 1 
  return dict_1


def most_common_letter(str2):
  """ Function to return maximum occuring letters """
  dict_2 = letter_counts(str2) 
  max_value = max(dict_2.values()) 
  return [key for key,value in dict_2.items() if value == max_value], max_value 


def string_count_histogram(str3):
  """ Function to print historgram like letters """
  dict_3 = letter_counts(str3)  

  for key in sorted(dict_3):  
    print(key * dict_3[key])  


if __name__ == '__main__':
  sentence = 'WHO WHAT WHERE WHEN WHY'
  print ("The string being analyzed is:", '"{}"'.format(sentence))
  print('Dictionary of letter counts:', letter_counts(sentence))
  most_frequent = most_common_letter(sentence)

  if len(most_frequent[0]) == 1:
    print('Most frequent letter "' + str(most_frequent[0][0]) + '" appears ' + str(most_frequent[1]) + ' times.')
  else:
    print('Most frequent letters ' + str(most_frequent[0]) + ' appears ' + str(most_frequent[1]) + ' times.')
  
  string_count_histogram(sentence)
