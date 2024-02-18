'''Write functions in Python called number of factors( ) and list of factors( ) that take a positive integer 
and do the following : 
(a) number_of_factors(val) : returns a list of its factors 
(b) list_of_factors(val):returns how many factors the number has. 
Check if input is positive and report if not. '''

def number_of_factors(val):
    if val < 0:
        return "Input is not positive"
    factors = []
    for i in range(1, val+1):
        if val % i == 0:
            factors.append(i)
    return factors

def list_of_factors(val):
    if val < 0:
        return "Input is not positive"
    return len(number_of_factors(val))

print(number_of_factors(12))
print(list_of_factors(12))