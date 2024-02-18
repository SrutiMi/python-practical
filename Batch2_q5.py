'''Write a program in Python that populates an empty list with integers, each which are either 0 or 1. Then 
find the size of the longest chain of zeros. Also give the span of indices containing the longest chain. 
For example
the longest run of zeros in [1,0,1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,1] is 6. 
span: 7 to 12'''

list1 = [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]
curr_count = 0
max_count = 0
start = None
end = None

for i, num in enumerate(list1):
    if num == 0:
        if curr_count == 0:
            start =i
        curr_count +=1
    else:
        if curr_count > max_count:
            max_count = curr_count
            
            end = i - 1
        curr_count = 0
        

# Check for the longest chain at the end of the list
if curr_count > max_count:
    max_count = curr_count
    end = len(list1) - 1
    start = end - max_count +1
start = end-max_count+1
print(f'The longest run of zeros in {list1} is {max_count}. Span: {start} to {end}')

