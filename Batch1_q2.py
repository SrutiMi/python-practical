''' Write a Python program to print all non-prime, non-Fibonacci numbers within range a-b, where a and b are accepted as command line arguments. '''

import math 
def non_prime(i):
  count=0
  for j in range(1,i+1):
    if i%j == 0:
      count+=1
  
  if count == 2 :
    return False
  return True
  
def perfect_square(i):
  sq_root =int(math.sqrt(i))
  if sq_root**2 == i:
    return True
  return False

def non_fibonacci(i):
  # N is a Fibonacci number if and only if ( 5*N^2 + 4 ) or ( 5*N^2 – 4 ) is a perfect square
  if perfect_square(5*i*i+4) or perfect_square(5*i*i-4):
    return False
  return True

a =int(input("Enter the value of a"))
b = int(input("Enter the value of b : "))

for i in range(a,b):
  if( non_prime(i) and non_fibonacci(i)):
    print(i,end =",")
