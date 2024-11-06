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