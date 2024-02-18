''' Write a Python program to simulate stack data structure using lists. Include standard stack operations like push( ). pop (). peek ( ) and is empty ( )'''

class Stack:
  def __init__(self):
    self.items = []

  def push(self,item):
    self.items.append(item)
    print(f"Pushed :{item} ")

  def pop(self):
    if not self.is_empty():
      popped_item = self.items.pop()
      print(f"Popped :{popped_item} ")
      return popped_item
    else:
      print("Stack is empty")

  def peek(self):
    if not self.is_empty():
      peeked_item = self.items[-1]
      print(f"Peeked :{peeked_item} ")
    else:
      print("Stack is empty")

  def is_empty(self):
    return len(self.items)==0
  
stack =Stack()
stack.push(10)
stack.push(20)
stack.push(30)

stack.peek()
stack.pop()
stack.peek()

    