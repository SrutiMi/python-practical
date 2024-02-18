'''. Write a program Python to implement a queue using list. Must incorporate the functions for 
add-element() delete element( ), list full( ) and list empty( )'''

class Queue:
  def __init__(self,max_size):
     self.queue = []
     self.max_size = max_size
  
  def add_element(self,element):
     if len(self.queue)< self.max_size:
       self.queue.append(element)
       return True
     else:
        print("Queue is full")
        return False
  
  def delete_element(self):
    if len(self.queue)>0:
      return self.queue.pop(0)
    else:
      print("Queue is empty")
      return False
  
  def list_full(self):
    return len(self.queue) == self.max_size
  
  def list_empty(self):
    return len(self.queue) == 0
  
queue = Queue(5)
print(queue.add_element(1))
print(queue.add_element(2))
print(queue.add_element(3))
print(queue.add_element(4))
print(queue.add_element(5))

print(queue.delete_element())
print(queue.queue)