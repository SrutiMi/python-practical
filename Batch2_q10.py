''' Write a program in Python that has a class namely PyWords. It has a field namely process-words that 
can store a list of words. The user of the class should pass a list of words as input to the class. 
There should be functions to solve the jobs given below :
(a) words_with _length(1) : returns a list of words that have length 1
(b) starts with(s) returns a list of all the words that start with s 
(c) palindromes() - returns a list of all the palindromes in the list, report if no palindrome exists in 
list
'''

class PyWords:
  def __init__(self, process_words):
    self.process_words = process_words
  
  def word_len(self,length):
    result = []
    for word in self.process_words:
      if len(word) == length:
        result.append(word)
    return result
  
  def starts_with(self, s):
    result = []
    for word in self.process_words:
      if word.startswith(s):
        result.append(word)
    return result
  
  def palindrome(self):
    result = []
    for word in self.process_words:
      if word == word[::-1]:
        result.append(word)
    
    if result:
      return result
    else:
      return "No palindrome exists in list"
    
words_list = ["level", "python", "radar", "hello", "civic", "world", "deed",'h','sruti']
py_words = PyWords(words_list)

length_one_words = py_words.word_len(1)
print(f"Words with length 1: {length_one_words}")

starts_with_s_words = py_words.starts_with("s")
print(f"Words starting with 's': {starts_with_s_words}")

palindrome_words = py_words.palindrome()
print(f"Palindromes: {palindrome_words}")
