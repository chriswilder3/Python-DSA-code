#  We can implement stack(LIFO) using 2 methods in Python 
    
# 1. using lists
mystack = []

    # Now here we push() items using normal append function
mystack.append(12)
mystack.append(8)
mystack.append(23)

    # Since the last element added is always at the end of list
    # we can consider end of list to be top of stack
    # hence list[-1] is same as stack.top() ie. access top of stack

print(mystack[-1]) # 23

    # Now stack pop() operation is handled by same operation on list pop()
    # it not only pops TOS, but also returns it

print(mystack.pop()) # 23
print(mystack[-1]) # 8 ,current TOS

# This method is simple but has disadvantages. Since list is dynamic array
# when capacity is runout it has to copy entire array to new location

# --------------------------------------------------

# 2. Another method is to use deque() from Python collections
    # collections is library/module in python that implements variaus
    # container types. The deque() is generalization of stacks and queues
    #  which is implemented using doubleLinkedList. Hence problem with
    # dynamic arrays doesnt exist for this

from collections import deque # Its a class in a library

mystack = deque() 
    # We can even specify maxlen as argument, if not specified it will
    # be unbound and maxlen is taken as None.
    # Lets use it as unbound stack first.

    # It has many functions even used for queue
    # But for stack main functions are : append(), pop(),
mystack.append(13)
mystack.append(35)
mystack.append(63)
mystack.append(28)

print(mystack) # deque([13, 35, 63, 28])

print(mystack.pop()) # 28
print(mystack) # deque([13, 35, 63])

# Hence LIFO strategy is being followed

# We can access TOS using -1 here also
print(mystack[-1]) # 63

#  For formal definition reasons we can form stack ADT class with only 
# stack methods.


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, item):
        self.container.append(item)
    
    def pop(self):
        return self.container.pop()
    
    def top(self):
        return self.container[-1]

    def size(self):
        return len(self.container) # Remember deque() works just like stack 
                                    # henc the len() applies too
    def isEmpty(self):
        return len(self.container) == 0

s = Stack()
s.push(32)
s.push(12)
print(s.top()) # 12
print(s.size()) #2
print(s.isEmpty()) # False
    

