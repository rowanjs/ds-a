def identity(x):
    return x

class OrderedRecordArray:
    def __init__(self, initialsize, key=identity):
        self.__a = [None] * initialsize
        self.__nItems = 0
        self.__key = key
    
    def __len__(self):
        return self.__nItems
    
    def get(self, n):
        if 0 <= n and n < self.__nItems:
            return self.__a[n]
        raise IndexError("Index "+ str(n) + " is out of range")
    
    def traverse(self, function=print):
        for i in range(self.__nItems):
            function(self.__a[i])
    
    def __str__(self):
        string = "["
        for i in range(self.__nItems):
            if len(string) > 1:
                string += ", "
            string += str(self.__a[i])
        string += "] "
        return string
    
    #binary search
    def find(self, key):
        lo = 0
        hi = self.__nItems - 1

        while lo <= hi:
            mid = (lo + hi) // 2

            if self.__key(self.__a[mid]) == key:
                return mid
             
            elif self.__key(self.__a[mid]) < key:
                lo = mid + 1
            
            else:
                hi = mid - 1
        
        return lo #item not found - return insertion point

    def search(self, key):
         idx = self.find(key)
         if idx < self.__nItems and self.__key(self.__a[idx]) == key:
             return self.__a[idx]
         
    def insert(self, item):
        if self.__nItems >= len(self.__a):
            raise Exception("Array overflow")

        idx = self.find(self.__key(item))

        for i in range(self.__nItems, idx, -1): #shifting existing to right
            self.__a[i] = self.__a[i-1]
        
        self.__a[idx] = item
        self.__nItems += 1
    
    def delete(self, item):
        idx = self.find(self.__key(item))
        if idx < self.__nItems and self.__a[idx] == item:
            self.__nItems -= 1
            for j in range(idx, self.__nItems):
                self.__a[j] = self.__a[j+1]
            return True
        return False
    
    def merge(self, other):
        if self.__key == other.__key:
            new_arr = OrderedRecordArray((len(self) + len(other)), key=self.__key)
            for i in range(self.__nItems):
                new_arr.insert(self.__a[i])
            for j in range(other.__nItems):
                new_arr.insert(other.__a[j])
            return new_arr
        raise KeyError("Keys of array objects do not match")






        
