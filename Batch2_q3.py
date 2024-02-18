''' Write a class in Python called PyConverter. User will pass a length and a unit when declaring an object from the class, for example ob = PyConverter (9, 'meters'). Consider units to be kilometers, meters and 
centimeters. For each of these units there should be a method that returns the length output converted 
into those units. For example, using the PyConverter object if the user calls ob.centimeter(), he should 
get 900 as the result. '''

class PyConverter:
  def __init__(self,length,unit):
    self.length = length
    self.unit = unit.lower()

  def kilometer(self):
    if self.unit == 'kilometers':
      return self.length
    elif self.unit == 'meters':
      return self.length /1000
    elif self.unit == 'centimeters':
      return self.length /100000
    
  def meter(self):
    if self.unit == 'kilometers':
      return self.length * 1000
    elif self.unit == 'meters':
      return self.length
    elif self.unit == 'centimeters':
      return self.length /100
    
  def centimeter(self):
    if self.unit == 'kilometers':
      return self.length * 100000
    elif self.unit == 'meters':
      return self.length * 100
    elif self.unit == 'centimeters':
      return self.length
    
ob =PyConverter(9,'meters')
print(ob.centimeter())
print(ob.kilometer())
print(ob.meter())