''' WAP to calculate the harmonic sum of n-1 terms of the series 1 + 1/2 + 1/3 + 1/4 + 1/5 + ... + 1/n.'''

def harmonic_sum(n):
    if n<=1:
        return 0
    sum = 0
    for i in range(1,n):
        sum += 1/i
    return sum

n = int(input("Enter the value of n: "))
result = harmonic_sum(n)

print(f"The harmonic sum of {n-1} terms is: {result}")