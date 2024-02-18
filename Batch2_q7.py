'''Write a program in Python to find all numbers between l and N those are divisible by 7 and end 
in 6. Also display their count. 
For example : if N = 60, list of numbers : [56], count = 1. 
(b) Write a program in Python to input different names in any case. Now convert the upper case letters to lower case and vice versa.'''

l = int(input("Enter the lower limit:"))
N = int(input("Enter the upper limit:"))

numbers = []
count =0
for i in range(l,N+1):
   if i % 7==0 and i%10==6:
      numbers.append(i)
      count +=1
print(f'List of numbers: {numbers}, count = {count}')

names =input("Enter names separated by spaces:").split()
converted_name = []
for name in names:
   converted_names=""
   for char in name:
      if 'A'<=char<='Z':
        converted_names +=chr(ord(char)+32)
      else:
        converted_names +=chr(ord(char)-32)
   converted_name.append(converted_names)

print(converted_name)