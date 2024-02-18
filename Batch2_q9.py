''' Write a program in Python to find a pair of elements (index pair) from a given array numbers whose 
sum equals a given target number. This target value is an user input. Report if a solution is found or not. 
Note that, there can be more than one solutions for a target input, so break out when one of them is 
found. 
Input : numbers = [10, 30, 20, 40, 50, 60, 70], target = 50 
Output : 0, 3 
1,2 '''

def find_pair(numbers,target):
  n = len(numbers)
  pairs = []

  for i in range(n-1):
    for j in range(i+1,n):
      if numbers[i]+numbers[j] == target:
        pairs.append((i,j))
  return pairs

# Example usage:
numbers = [10, 30, 20, 40, 50, 60, 70]
target = int(input("Enter the target sum: "))

result = find_pair(numbers, target)

if result:
    print("Output:")
    for pair in result:
        print(pair[0], ",", pair[1])
else:
    print("No pairs found with the given target sum.")