# Hash are implemented in Python using Dictionaries.
# We will implemented hash using simple ASCII hash fun
# Note that ord(char) gives ASCII val of the char.
# In this program, we will just implement simple one 
# In the next version, We will implement collision handling also

def get_hash(key): # Hash funn
    h = 0 
    for char in key:        # For every char in key string add their ASCII
        h += ord(char)      # do sum%100. This means tablesize is 100
    return h % 100          # this returns the position mapped in the table 


print(ord('1'), ord('a'), ord('z'),ord('A'),ord(" ")) # 49 97 122 65 32

print(get_hash('mykey1')) # 8
print(get_hash('mykey'))  # 59
print(get_hash('sdad'))   # 12, So different keys(str) give different hash

print("--------------------------")

# Lets create Class which acts as hashtable with hash fun as its method

class myHashTable:
    def __init__(self):
        self.MAX = 100      # size of table, We can change it if we want
        self.arr = [ None for i in range(self.MAX)] # Intialize arr with Null vals

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h% self.MAX

    def add(self, key, val): # actual user input is taken as key-val pair
        h = self.get_hash(key)
        self.arr[h] = val

    def get(self, key):   # similar to accessing by mydict[key]
        h = self.get_hash(key)
        return self.arr[h]

    # Python allows us overload operators, Hence we can modify our class to
    # allow access just like dictionary. mydict[key] 
    # We need to rename our methods to __getitem__ and __setitem__ for this
    
    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]
    
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val


t = myHashTable()
# print(t.get_hash('sachin'))
t.add('sachin',23)
t.add('mach', 12)
t.add('jake',35)
# print(t.get('sachin'))  # 23
# print(t.get('mach'))  # 12
# print(t.get('dags'))  # None

# Now due to overoad of get and set item function we can do this
print(t['sachin']) # 23
t['track'] = 78
print(t['track']) # 78


# We still need to implement collision handling..