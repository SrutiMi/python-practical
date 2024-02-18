'''Write a program in Python to use the file data.txt for solving and displaying outputs the following tasks 
after reading it: 
(a) All words ending with "on"
b) All words whose second and third letters are "r" and "e"
(c) All words with no vowels

 '''

def word_end_on(file_content):
  result = []
  words = file_content.split()
  for word in words:
    if word.lower().endswith('on'):
      result.append(word)
  return result

def word_2nd_3rd(file_content):
  result=[]
  words = file_content.split()
  for word in words:
    if len(word)>=3 and word[1] == 'r' and word[2] =='e':
      result.append(word)
  return result

def words_no_vowel(file_content):
  result = []
  vowel='aeiouAEIOU'
  words = file_content.split()
  for word in words:
    has_no_vowels = True
    for char in word:
      if char.lower() in vowel:
        has_no_vowels = False
        break
    if has_no_vowels:
      result.append(word)
  return result

try:
  with open('input.txt','r') as file:
     file_content= file.read()

  print("Words ending with 'on' :",word_end_on(file_content))
  print("Words whose second and third letters are 'r' and 'e' :",word_2nd_3rd(file_content))
  print("Words with no vowels :",words_no_vowel(file_content))
except FileNotFoundError:
  print("File not found")
except Exception as e:
  print(e)