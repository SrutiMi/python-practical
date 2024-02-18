'''Given a string S of lower case characters. The task is to check whether the given string is Heterogram 
or not. A heterogram is a word, phrase, or sentence in which no letter of the alphabet occurs more than 
once. Examples :
Input : S = "the big dwarf only jumps"
Output : Yes
Each letter in the string S has occurred only once. Write a program in Python to perform the said task.

'''

def is_heterogram(s):
  char_count ={}

  for char in s:
    if char!=' ':
      if char in char_count:
        return False
      else:
        char_count[char]=1

  return True

S="the big dwarf only jumps"
result =  is_heterogram(S.lower())

if result:
  print("Yes")
else:
  print("No")