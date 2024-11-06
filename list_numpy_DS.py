# Python Data Structures and NumPy Basics

# 1. LISTS
# Lists are ordered, mutable, and can contain duplicates.
nums = [3, 1, 4, 1, 5]
nums.append(9)  # Adds 9 to the end of the list
nums.sort()     # Sorts the list in ascending order
squared_nums = [x**2 for x in nums if x > 2]  # List comprehension with condition

# 2. TUPLES
# Tuples are ordered, immutable, and can contain duplicates.
point = (2, 3)
x, y = point  # Tuple unpacking
points_list = list(point)  # Convert tuple to list for mutability

# 3. SETS
# Sets are unordered, mutable, and contain unique elements.
unique_nums = {1, 2, 3}
unique_nums.add(2)  # No effect, as 2 is already in the set
unique_nums.remove(1)  # Removes 1 from the set
# Set operations
set_a = {1, 2, 3}
set_b = {2, 3, 4}
union_set = set_a | set_b           # {1, 2, 3, 4}
intersection_set = set_a & set_b     # {2, 3}
difference_set = set_a - set_b       # {1}

# 4. DICTIONARIES
# Dictionaries store key-value pairs and are mutable.
student = {"name": "Alice", "age": 22}
student["grade"] = "A"  # Adds a new key-value pair
age = student.get("age", "Not found")  # Returns age or "Not found" if key doesn't exist
for k, v in student.items():  # Iterating over dictionary items
    print(f"{k}: {v}")

# 5. STACKS (LIFO)
# Stack can be implemented using a list.
stack = []
stack.append(1)  # Push element
stack.append(2)
top = stack.pop()  # Pop element (LIFO behavior)

# 6. QUEUES (FIFO)
# Queue can be implemented using collections.deque for efficient append and pop from both ends.
from collections import deque
queue = deque([1, 2, 3])
queue.append(4)     # Enqueue element
first_in = queue.popleft()  # Dequeue element (FIFO behavior)

# 7. NUMPY BASICS
# Importing NumPy for efficient array handling
import numpy as np

# Array Creation
arr = np.array([1, 2, 3])        # 1D array
matrix = np.ones((2, 3))         # 2x3 matrix filled with 1s
zeros_matrix = np.zeros((2, 2))  # 2x2 matrix filled with 0s
random_matrix = np.random.rand(3, 3)  # 3x3 matrix with random values

# Indexing and Slicing
element = arr[1]              # Accessing single element
row_slice = matrix[1, :]      # Accessing a specific row
col_slice = matrix[:, 1]      # Accessing a specific column
sub_matrix = matrix[0:2, 0:2] # Slicing a sub-matrix

# Summary
# This code covers:
# - Lists, tuples, sets, and dictionaries as basic data structures
# - Stack and Queue implementations using lists and deque
# - Basic array handling using NumPy for numerical operations
