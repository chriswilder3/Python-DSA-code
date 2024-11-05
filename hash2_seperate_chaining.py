#  We will implement seperate chaining first.
# Here in this class before we will initialize array with [], not None
# since we want to access key val pairs of chain 

# Also lets reduce arr size to 10, to allow more collisions for demonstration

class myHashTable:
    def __init__(self):
        self.MAX = 10  
        self.arr = [ [] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

# We know that for seperate chaining we use LinkedList. But in Python
# we have alternative to this. We use list of tuples here.
# so at each 'h' location in arr, exists a list of tuples

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False

        # we first need to check whether key is already in this 'h' location
        for ind,entry in enumerate(self.arr[h]): 
            if len(entry) == 2 and entry[0] ==key: # each entry in this list is a tuple
                self.arr[h][ind] = (key, val)
                # we cant do entry[1] = val, since tuple are immutable
                found = True

        if found == False: # If the key doesnt exist already in that list
                            # We need to enter this new key,val into it
            self.arr[h].append( (key,val))

    def __getitem__(self, key):
        h = self.get_hash(key)
        
        found = False
        # Now we should iterate through list at 'h' location and give the 
        # val in the tuple correspnding to key
        for entry in self.arr[h]:
            if entry[0] == key:
                found = True
                return entry[1]
        if found == False:
            raise KeyError(f' {key} is not hashed')
            
    def __delitem__(self, key):
        # This is used to delete entry correspoding to key
        h = self.get_hash(key)
        delInd = None
        for ind,entry in enumerate(self.arr[h]):
            if entry[0] == key:  
                delInd = ind  # We can delete directly this index also using
                              # del self.arr[h][ind]
                              
        if delInd == None:
            print(' No such key to delete')
        else:
            self.arr[h].pop(delInd) # Remember pop(ind) for delete by index 
                                    # remove(val) for delete by val


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