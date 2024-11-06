#  Implementation With Lists
# In queue FIFO works, So elements must be always be inserted from one end
# and always discarded from other


myqueue = []

# Insertion works when we insert always at the start(rear)
# This is called Enqueue() operation
myqueue.insert(0,12)
myqueue.insert(0,36)
myqueue.insert(0,27)

print(myqueue)
# We can look and front and rear elements, usually with pointers
# but here, -1 and 0 index work
print( f' front : {myqueue[-1]}' )
print( f' rear : {myqueue[0]}' )

# We can delete from front
# This is called Dequeue() operation
print(myqueue.pop())
print(myqueue)

# But just like stacks, queue with lists is not good tactic
# Again we can use collections.deque for this
# Remember its deque NOT dequeue
from collections import deque

myqueue = deque()

# Note that the dequeue() has a method called appendleft() which could 
# be used for enqueue. 
myqueue.appendleft(10)
myqueue.appendleft(20)
myqueue.appendleft(30)
myqueue.appendleft(40)

print(myqueue) # deque([40, 30, 20, 10])

# Dequeue works as before with pop()
print(myqueue.pop()) # 10

# acess the front and rear elems
print(myqueue[-1]) # 20
print(myqueue[0]) # 40

# Similar to before we can implement a proper class implementation of queue

