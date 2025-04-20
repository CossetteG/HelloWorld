# import whatever you need here
import time
import sys

class HashMap:
    class HashNode:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next = None

    def __init__(self, size=7):
        self._size = size
        self.vals = [None]*size

    def hash(self, key):
        r = key[0]
        c = key[1] + 1
        return (r*c)%self._size
    
    def capacity(self):
        filled = 0

        for i in range(self._size):
            if (self.vals[i]==None):
                pass
            else: filled +=1

        return filled/self._size

    def get(self, key):
        index = self.hash(key) 

        if (self.vals[index]==None):
            return None
        elif (self.vals[index].key == key):
            return self.vals[index].value
        
        elif (self.vals[index].next ==None):
            return None
        elif (self.vals[index].next.key == key):
            return self.vals[index].next.value
        
        elif (self.vals[index].next.next ==None):
            return None
        elif (self.vals[index].next.next.key == key):
            return self.vals[index].next.next.value
        
        else: 
            return None
        

    def set(self, key, value, existing=None):
        index = self.hash(key)

        if (existing==None):
            newnode = self.HashNode(key, value)
        else:
            newnode = existing

        if (self.vals[index]==None):
            self.vals[index] = newnode
        elif (self.vals[index].next == None):
            self.vals[index].next = newnode
        elif (self.vals[index].next.next == None):
            self.vals[index].next.next = newnode
        else:
            self.vals[index].next.next.next = newnode
            self.rehash()

        if (self.capacity() >= .8):
            self.rehash()

    def remove(self, key):
        index = self.hash(key) 
        mnode = None

        if (self.vals[index].key == key):
            mnode = self.vals[index]
            self.vals[index] = mnode.next
            mnode.next = None
        elif (self.vals[index].next.key == key):
            mnode = self.vals[index].next
            self.vals[index].next = mnode.next
            mnode.next = None
        elif (self.vals[index].next.next.key == key):
            mnode = self.vals[index].next.next
            self.vals[index].next = mnode.next
            mnode.next = None
        else: 
            raise ValueError("key not found")
    
        return mnode

    def clear(self):
        self._size = 7
        self.vals = [None]*7
    
    def size(self):
        return self._size
    
    def keys(self):
        keylist = []

        for i in range(self._size):
            bucket = self.vals[i]

            while(bucket != None):
                keylist.append(self.remove(bucket.key))
                bucket = self.vals[i]

        for k in keylist:
            if (k==None):
                raise ValueError("invalid key in list")

        return keylist

    def rehash(self):
        newsize = self._size*2-1 
        nodes = self.keys()
        
        self._size = newsize
        self.vals = [None]*newsize

        for node in nodes:
            self.set(node.key, node.value)

count = 0
# Part 1 -- Write weight_on_cacheless() method
def weight_on_cacheless(r,c): 
    global count

    if ((c < 0) or (c > r)):
        return 0

    if (r==0):
        count = count+1
        return 200
    
    left = weight_on_cacheless(r-1, c-1)
    right = weight_on_cacheless(r-1, c)
    
    count = count+1
    return 200 + (left + right)/2

cache = HashMap()
hits = 0
# Part 3 -- Write weight_on_with_caching() method
def weight_on_with_caching(r,c):
    global cache
    global count
    global hits
    got = cache.get((r,c))

    if (got==None):
        if ((c < 0) or (c > r)):
            return 0

        if (r==0):
            count = count+1
            cache.set((r,c),200)
            return 200
        
        left = weight_on_with_caching(r-1, c-1)
        right = weight_on_with_caching(r-1, c)
        
        count = count+1
        newval = 200 + (left + right)/2
        cache.set((r,c),newval)
        return newval
    else:
        hits +=1
        count += 1
        return got


def main():
    # Part 2 -- Use weight_on_cacheless() method
    # Cacheless
    print("Cacheless:")
    start = time.perf_counter()
    global count
    i = 0
    num = 7
    # num = int(sys.argv[1])
    f = open("cacheless.txt","w")
    while i < num:
        j = 0
        row = ""
        while j <= i:
            row += '{:.2f}'.format((weight_on_cacheless(i,j)-200)) + " "
            j+=1
        print(row)
        f.write(row + '\n')
        i+=1
    elapsed = time.perf_counter() - start
    print("\nElapsed time: " + str(elapsed) + " seconds.")
    f.write("\nElapsed time: " + str(elapsed) + " seconds." + '\n')
    print("Number of function calls: " + str(count) )
    f.write("Number of function calls: " + str(count) )
    f.close()

    # Part 3 -- Use weight_on_with_caching() method, with your HashMap ADT
    print("\nWith Cache:")
    start = time.perf_counter()
    i = 0
    f = open("with_caching.txt","w")
    global hits
    count = 0
    while i < num:
        j = 0
        row = ""
        while j <= i:
            row += '{:.2f}'.format((weight_on_with_caching(i,j)-200)) + " "
            j+=1
        print(row)
        f.write(row + '\n')
        i+=1
    elapsed = time.perf_counter() - start
    print("\nElapsed time: " + str(elapsed) + " seconds.")
    f.write("\nElapsed time: " + str(elapsed) + " seconds." + '\n')
    print("Number of function calls: " + str(count) )
    f.write("Number of function calls: " + str(count) )
    print("Number of cache hits: " + str(hits) )
    f.write("Number of cache hits: " + str(hits) )
    f.close()

    # Part 2.5 write and test the Hash ADT
    # print('\n')
    # teth = HashMap()            #init, HashNode, set, get // 'A'
    # teth.set((0,0), 'A') 
    # print(teth.get((0,0)))

    # print(teth.hash((0, 0)))    #hash // 0, 4, 3
    # print(teth.hash((2, 1)))
    # print(teth.hash((3, 0)))

    # print(teth.capacity())      #capacity, keys, size, clear
    # print(teth.keys())
    # print(teth.size())
    # teth.clear()
    # print(teth.capacity())      
    # print(teth.keys())

    # teth.set((3,0), 'A')        #set, rehash(chain), capacity, get(after rehash), keys(after rehash), remove(keynot found)
    # teth.set((1,0), 'B')        #found a bug in my remove function here- i forgot to reset the chains
    # teth.set((1,0), 'C')
    # teth.set((8,0), 'D')
    # print(teth.capacity())
    # # print(teth.get((0,0)))
    # print(teth.get((1,0)))
    # # print(teth.keys()) 

    # teth.clear()                #rehash(capacity)
    # teth.set((1,0), 'p')
    # teth.set((2,0), 'o')
    # teth.set((3,0), 'i')
    # teth.set((4,0), 'u')
    # teth.set((5,0), 'y')
    # print(teth.capacity())
    # print(teth.size())
    # teth.set((6,0), 't')
    # print(teth.capacity())
    # print(teth.size())



if __name__=="__main__":
    main()



#VERSION 2

# class HashMap:
#     class HashNode:
#         def __init__(self, key, value):
#             self.key = key
#             self.value = value
#             self.next = None

#     def __init__(self, size=7):
#         self._size = size
#         self.vals = [None]*size
#         self.osize = 0

#     def hash(self, key):
#         r = key[0]
#         c = key[1] + 1
#         return (r*c)%self._size
    
#     def calccapacity(self):
#         filled = 0

#         for i in range(self._size):
#             if (self.vals[i]==None):
#                 pass
#             else: filled +=1

#         return filled/self._size
        
#     def capacity(self):
#         if (self._size == 7):
#             return self._size
#         else:
#             return self._size + 1

#     def getb(self, key):
#         index = self.hash(key) 

#         if (self.vals[index]==None):
#             return None
#         elif (self.vals[index].key == key):
#             return self.vals[index].value
        
#         elif (self.vals[index].next ==None):
#             return None
#         elif (self.vals[index].next.key == key):
#             return self.vals[index].next.value
        
#         elif (self.vals[index].next.next ==None):
#             return None
#         elif (self.vals[index].next.next.key == key):
#             return self.vals[index].next.next.value
        
#         else: 
#             return None


#     def get(self, key):
#         index = self.hash(key) 
#         interest = 0

#         if (self.vals[index]==None):
#             raise KeyError
#         elif (self.vals[index].key == key):
#             interest = self.vals[index].value
        
#         elif (self.vals[index].next ==None):
#             raise KeyError
#         elif (self.vals[index].next.key == key):
#             interest = self.vals[index].next.value
        
#         elif (self.vals[index].next.next ==None):
#             raise KeyError
#         elif (self.vals[index].next.next.key == key):
#             interest = self.vals[index].next.next.value 
        
#         return interest -200

#     def set(self, key, value, existing=None):
#         index = self.hash(key)

#         if (existing==None):
#             newnode = self.HashNode(key, value)
#         else:
#             newnode = existing

#         if (self.vals[index]==None):
#             self.vals[index] = newnode
#         elif (self.vals[index].next == None):
#             self.vals[index].next = newnode
#         elif (self.vals[index].next.next == None):
#             self.vals[index].next.next = newnode
#         else:
#             self.vals[index].next.next.next = newnode
#             self.rehash()

#         self.osize += 1
#         if (self.calccapacity() >= .8):
#             self.rehash()

#     def remove(self, key):
#         index = self.hash(key) 
#         mnode = None

#         if (self.vals[index].key == key):
#             mnode = self.vals[index]
#             self.vals[index] = mnode.next
#             mnode.next = None
#         elif (self.vals[index].next.key == key):
#             mnode = self.vals[index].next
#             self.vals[index].next = mnode.next
#             mnode.next = None
#         elif (self.vals[index].next.next.key == key):
#             mnode = self.vals[index].next.next
#             self.vals[index].next = mnode.next
#             mnode.next = None
#         else: 
#             raise ValueError("key not found")
    
#         self.osize -=1
#         return mnode
        

#     def clear(self):
#         self._size = 7
#         self.vals = [None]*7
    
#     def size(self):
#         return self.osize
    
#     def keysb(self):
#         keylist = []

#         for i in range(self._size):
#             bucket = self.vals[i]

#             while(bucket != None):
#                 keylist.append(self.remove(bucket.key))
#                 bucket = self.vals[i]

#         for k in keylist:
#             if (k==None):
#                 raise ValueError("invalid key in list")

#         return keylist
    
#     def keys(self):
#         keylist = []

#         for i in range(self._size):
#             bucket = self.vals[i]

#             while(bucket != None):
#                 keylist.append(self.remove(bucket.key).key)
#                 bucket = self.vals[i]

#         for k in keylist:
#             if (k==None):
#                 raise ValueError("invalid key in list")

#         return keylist

#     def rehash(self):
#         newsize = self._size*2-1 
#         nodes = self.keysb()
        
#         self._size = newsize
#         self.vals = [None]*newsize

#         for node in nodes:
#             self.set(node.key, node.value)


