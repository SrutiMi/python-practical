''' Write a Python program that defines a class Length, which models length in feet and inches. 
Include the following class methods : 
(a) A constructor that initializes length (default values will be 0). 
(b) SetLength ( ) : To set value of feet and inches. 
(c) getLength ( ) : To return feet-inches in a tuple. 
(d) A magic method to print length. 
(e) A magic method to add two lengths. '''

class Length:

  def __init__(self,feet=0,inches=0):
    self.feet=feet
    self.inches=inches

  def setLength(self,feet,inches):
    self.feet = feet
    self.inches = inches
  
  def getLength(self):
    return (self.feet,self.inches)
  
  def __str__(self):
    return f"{self.feet} feet , {self.inches} inches"
  
  def __add__(self,other):
    total_feet = self.feet + other.feet
    total_inches = self.inches + other.inches

    if total_inches >=12:
      total_feet += total_inches //12
      total_inches %=12

    return Length(total_feet, total_inches) #returning a length object 
  
length1 = Length()
length1.setLength(12,12)

length2 = Length()
length2.setLength(5,5)

print("Length 1:", length1)
print("Length 2:", length2)

# Adding two lengths
total_length = length1 + length2
print("Total Length:", total_length)