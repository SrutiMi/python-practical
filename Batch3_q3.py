'''Given a string write a program in Python to find the occurrences of every character, number, special 
character, punctuations etc.'''

def count_occurrences(string):
    occurrences = {}
    for char in string:
        if char in occurrences:
            occurrences[char] += 1
        else:
            occurrences[char] = 1
    return occurrences

string = "Hello,$$$ 123 World!"
result = (count_occurrences(string))

for i,j in result.items():
    print(i,":",j)