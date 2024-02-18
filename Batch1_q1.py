'''Write a Python function expanding (numlist), that takes as argument a list of integers, numlist[], and 
returns True if the absolute difference between each adjacent pair of elements strictly decreases; and 
False otherwise. Write a driver program to test the function. The function should handle necessary 
validation checks '''

def expanding(numlist):
  if len(numlist)<2: 
    print("Please atleas enter 2 numbers.")
    return False
  
  for i in range(1, len(numlist)-1):

    diff1= abs(numlist[i] - numlist[i-1])
    diff2 = abs(numlist[i+1] - numlist[i])

    if diff2>=diff1:
      return False
    
  return True

#Driver program

numlist = [1, 3, 7, 2, 9]
print(expanding(numlist)) 

numlist = [1, 3, 7, 2, 0]
print(expanding(numlist))

numlist = [2, 10, 16, 20]
print(expanding(numlist))