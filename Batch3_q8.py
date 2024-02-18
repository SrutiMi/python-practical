'''(b) Write a Python program to check whether a given number is Armstrong. 
A number is called an Armstrong number if it is equal to the sum of its own digits raised to the power of the number of digits.'''

def armstrong(number):
  num_str = str(number)
  num_dg= len(num_str)

  armstrong_sum = 0
  for dg in num_str:
     armstrong_sum +=int(dg)**num_dg
  
  return armstrong_sum == number

input_number = int(input("Enter a number: "))

if armstrong(input_number):
    print(f"{input_number} is an Armstrong number.")
else:
    print(f"{input_number} is not an Armstrong number.")