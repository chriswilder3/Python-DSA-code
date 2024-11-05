# Lets Implement Linear probing
# In linear probing, size is limited. It can overflow
# We will also have list of lists. But inner contains single key-val pair
# we took it as array not tuple since its mutable. But initially entries
# will be None for easy comparison.

# Also lets reduce arr size to 10, to allow more collisions for demonstration

class myHashTable:
    def __init__(self):
        self.MAX = 10  
        self.arr = [ None for i in range(self.MAX)] # for easier comparison
        self.length = 0

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

# We know that for seperate chaining we use LinkedList. But in Python
# we have alternative to this. We use list of tuples here.
# so at each 'h' location in arr, exists a list of tuples

    def __setitem__(self, key, val):
        if self.length == self.MAX:
            print(' The hashtable has overflown. No more items')
            return
        h = self.get_hash(key)
        found = False
        print(f' hash for {key} : {h}')
    # we first need to check whether anotherkey/ same key is already in this 'h' location
        if self.arr[h] == None or self.arr[h][0] == key:
            self.arr[h] = [key, val]
            self.length += 1
        else:   
            displaced_h = (h+1)%self.MAX # Linear probing
            while displaced_h != (h+self.MAX-1)% self.MAX: # untill u circle around
                if self.arr[displaced_h] == None or self.arr[displaced_h][0] == key:
                    self.arr[displaced_h] = [key, val]
                    self.length += 1
                    break
                displaced_h = (displaced_h+1)% self.MAX
        
    def __getitem__(self, key):
        h = self.get_hash(key)
        
        found = False
        # We use && shortcircuit to decide if entry exists and which one
        if self.arr[h] != None and self.arr[h][0] == key:
            # We hit the first place only
            found = True
            return self.arr[h][1]
        else:
            # Linear probing
            displaced_h = (h+1)%self.MAX # Linear probing
            while displaced_h != (h+self.MAX-1)% self.MAX:
                if self.arr[displaced_h] != None and self.arr[displaced_h][0] == key:
                    found = True
                    return self.arr[displaced_h][1]
                displaced_h = (displaced_h+1)% self.MAX
        if found == False:
            raise KeyError(f' {key} is not hashed')
            
    def __delitem__(self, key):
        # This is used to delete entry correspoding to key
        h = self.get_hash(key)

        deleted = False
        
        if self.arr[h] != None and self.arr[h][0] == key:
            # We need to delete the entry from this h
            deleted = True
            self.arr[h] = None
        else:
            # Linear probing
            displaced_h = (h+1)% self.MAX
            while displaced_h != (h+self.MAX-1)% self.MAX:
                if self.arr[displaced_h] != None and self.arr[displaced_h][0] ==key:
                    #found the element to delete
                    self.arr[displaced_h] = None
                    deleted = True
                    break
                displaced_h = (displaced_h+1)% self.MAX
        if deleted == False:
            print(' No such key to delete')
                       

ht = myHashTable()
print(ht.get_hash('march 6'), ht.get_hash('march 17')) # 9
# Hence these two produce collisions, which will now be handled 
# by our chain method
ht.__setitem__('march 6',12)
ht.__setitem__('march 7',23)
ht.__setitem__('march 17',54)
print(ht.arr)
# O/P :
# [[('march 7', 23)], [], [], [], [], [], [], [], 
# [], [('march 6', 12), ('march 17', 54)]]

# We can see that there are 10 lists corresponding to each 'h' location in hash
# two vals are map to same location since h = 9 for both, so
# the list correspoding to this at 10th location i.e h=9 (since h is 0-based)
# These two tuple in the list correspond to key, val pairs handled by chian method

# Lets also test newer get funcn

print(ht['march 7']) # 23
print(ht['march 6']) # 12
print(ht['march 17']) # 54
# print(ht['march 32']) # march 32 is not hashed

# Lets test del also
del ht['march 32'] #  No such key to delete
del ht['march 7']
print(ht.arr) # [[], [], [], [], [], [], [], [], [], [('march 6', 12), ('march 17', 54)]]

del ht['march 17']
print(ht.arr) # [[], [], [], [], [], [], [], [], [], [('march 6', 12)]]