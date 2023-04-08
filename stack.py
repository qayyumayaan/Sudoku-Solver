# Custom stack implementation in Python
class Stack:

    # Constructor to initialize the stack
    def __init__(self, size):
        self.arr = [None] * size
        self.capacity = size
        self.top = -1
 
    # Function to add an element `val` to the stack
    def push(self, val):
        if self.isFull():
            print('Stack Overflow!! Calling exit()…')
            exit(-1)
 
        # print(f'Inserting {val} into the stack…')
        self.top = self.top + 1
        self.arr[self.top] = val
 
    # Function to pop a top element from the stack
    def pop(self):
        # check for stack underflow
        if self.isEmpty():
            print('Stack Underflow!! Calling exit()…')
            exit(-1)
 
        # print(f'Removing {self.peek()} from the stack')
 
        # decrease stack size by 1 and (optionally) return the popped element
        top = self.arr[self.top]
        self.top = self.top - 1
        return top
 
    # Function to return the top element of the stack
    def peek(self):
        if self.isEmpty():
            exit(-1)
        return self.arr[self.top]
 
    # Function to return the size of the stack
    def size(self):
        return self.top + 1
 
    # Function to check if the stack is empty or not
    def isEmpty(self):
        return self.size() == 0
 
    # Function to check if the stack is full or not
    def isFull(self):
        return self.size() == self.capacity