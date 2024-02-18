'''Write a Pvthon program to input two sets, S1 and S2 containing names of cities. Then perform the 
following 
(a) Find union, intersection and symmetric diflerence of the two sets, 
(b) Display elements of Sl in upper case and s2 in lower case.  '''

def union(S1,S2):
  union_set =set()

  for city in S1:
    union_set.add(city)
  
  for city in S2:
    union_set.add(city)

  return union_set

def find_intersection(S1,S2):
  intersection_set = set()
  for city in S1:
    if city in S2:
      intersection_set.add(city)
  return intersection_set

def symmetric_difference(S1,S2):
  symmetric_diff_set = set()
  for city in S1:
    if city not in S2:
      symmetric_diff_set.add(city)
  for city in S2:
    if city not in S1:
      symmetric_diff_set.add(city)
  return symmetric_diff_set

def display_upper_lower(S1,S2):
   uppercase = {city.upper() for city in S1}
   lowercase = {city.lower() for city in S2}
   print(uppercase)
   print(lowercase)

S1 = set(input("Enter cities for S1(comma-separated):").split(','))  
S2 = set(input("Enter cities for S2(comma-separated):").split(','))

print("Union of S1 and S2:", union(S1,S2))
print("Intersection of S1 and S2:", find_intersection(S1,S2))
print("Symmetric Difference of S1 and S2:", symmetric_difference(S1,S2))
print("Displaying S1 in upper case and S2 in lower case:")
display_upper_lower(S1,S2)