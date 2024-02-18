'''Write a recursive Python function to check whether an integr is passed as an argument is a magic number or not .The function should check if the argument is not an integer '''

def digit_sum(number):

  if(number<10):
    return number
  
  curr_sum=0
  while number>0:
    curr_sum += number%10
    number //=10

  return digit_sum(curr_sum)

def is_magic(num):
  if not isinstance(num,int):
    print("Error -> Input is not an integer.")
    return False
  
  if num<10:
     return num ==1
  
  return is_magic(digit_sum(num))


try:
  number = int(input("Enter the integer : "))
  result = is_magic(number)

  if result:
    print(f"{number} is a magic number!")
  else:
    print(f"{number} is not a magic number!")

except ValueError:
  print("Error -> Input is not an integer.")