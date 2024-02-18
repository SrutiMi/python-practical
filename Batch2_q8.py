'''Write a program in Python to simulate stack operations using list (PUSH, POP, PEEP). Also check for overflow , underflow conditions in a regular stack'''

class Stack:
    def __init__(self, max_size):
        self.stack = []
        self.max_size = max_size

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.max_size

    def push(self, item):
        if self.is_full():
            print("Stack Overflow: Cannot push element, the stack is full.")
        else:
            self.stack.append(item)
            print(f"Pushed {item} into the stack.")

    def pop(self):
        if self.is_empty():
            print("Stack Underflow: Cannot pop element, the stack is empty.")
            return None
        else:
            popped_item = self.stack.pop()
            print(f"Popped {popped_item} from the stack.")
            return popped_item

    def peep(self):
        if self.is_empty():
            print("Stack is empty.")
            return None
        else:
            print(f"Peeked at the top of the stack: {self.stack[-1]}")
            return self.stack[-1]

# Example usage:
stack_size = 5
stack = Stack(stack_size)

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

stack.push(6)  # Overflow condition

stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()

stack.pop()  # Underflow condition

stack.peep()
