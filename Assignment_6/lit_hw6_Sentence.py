"""
Tianyi Li
Class: CS 521 - Summer 2
Date: 17 August 2021
Homework Problem # 1
Description of Problem: Write a python class library that evaluates\
and manipulates an English sentence.
"""
import re
import random
import unittest

class Sentence:

  def __init__(self,sentence=""):
    sentence= re.sub(r'[^\w\s]', '',sentence)
    self._sentence = re.findall(r'\w+', sentence)

  def get_all_words(self):
    return self._sentence

  def get_word(self,num_desired_word):
    return self._sentence[num_desired_word-1]

  def set_word(self,index,new_word):
    self._sentence[index] = new_word

  def scramble(self):
    copy = self._sentence.copy();
    random.shuffle(copy);
    return copy;

  def __repr__(self):
    return " ".join(self._sentence)

class TestSentence(unittest.TestCase):
    def setUp(self):
      self.sentence = Sentence("The lion chases the leopard.")

    def test_get_all_words(self):
        self.assertEqual(self.sentence.get_all_words(),["The","lion","chases","the","leopard"])

    def test_get_word(self):
        self.assertEqual(self.sentence.get_word(2),"lion")
        self.assertEqual(self.sentence.get_word(5),"leopard")

    def test_set_word(self):
        self.sentence.set_word(1,"tiger")
        self.sentence.set_word(4,"lion")
        self.assertEqual(self.sentence.__repr__(),"The tiger chases the lion")
        print("\n\nSentence worked correctly")
        print("\nThe final version of sentance: ")
        print(self.sentence)

    def test_scramble(self):
      copy = self.sentence.get_all_words().copy();
      scrambled = self.sentence.scramble()
      self.assertEqual(self.sentence.get_all_words(),copy)
      self.assertNotEqual(self.sentence.get_all_words(),scrambled)
    
    def test_repr(self):
      self.assertEqual(self.sentence.__repr__(),"The lion chases the leopard")

if __name__ == '__main__':
    unittest.main()




