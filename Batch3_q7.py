'''Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically

Input: green-red-yellow-black-white
Output: black-green-red-white-yellow
'''
def bubble_sort(words):
  for i in range(len(words)-1):
    for j in range(len(words)-i-1):
      if words[j]>words[j+1]:
        words[j],words[j+1]= words[j+1],words[j]

def sort_hyphen_separate(sequence):
  words=sequence.split('-')
  bubble_sort(words)
  sorted ='-'.join(words)
  return sorted

input_sequence = "green-red-yellow-black-white"
result = sort_hyphen_separate(input_sequence)
print("Output:", result)