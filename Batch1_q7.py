'''Write a recursive function that finds the H.CF. of two numbers passed as arguments. Then write a 
Pyhon program to input a list of integers, intlist[] and find the H.C.F. of the first and the fith elements. 
The program should handle errors like Name Error, Index Error, Zero Division Error and Value 
Error. '''

def hcf(x,y):

  if y==0:
    return x
  else:
    return hcf(x,x%y)
  
def list(intlist):

  try:
    if len(intlist)<5 :
      raise IndexError("List should have atleast 5 elements")
    first_element = intlist[0]
    fifth_element = intlist[4]
    if first_element ==0 or fifth_element ==0:
      raise ZeroDivisionError("Cannot calculate HCF with zero")
    
    hcf_result = hcf(first_element,fifth_element)
    return hcf_result
  except IndexError as e:
    return e
  except ZeroDivisionError as e:
    return e
  except ValueError as e:
    return e
  except Exception as e:
    return e
  

try:
  input = [12,24,36,48,60]
  result = list(input)
  print(f"The hcf of the first and fifth element is : {result}")
except NameError as e:
  print(e)
except Exception as e:
  print(e)