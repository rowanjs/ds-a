class Array:
    def __init__(self, initialsize):
       self.__a =  [None] * initialsize
       self.__nItems = 0
    
    def __len__(self):
        return self.__nItems
    
    def get(self, n):
        if 0 <= n and n < self.__nItems:
            return self.__a[n]
    
    def set(self, n, value):
        if 0 <= n and n < self.__nItems:
            self.__a[n] = value
    
    def insert(self, item):
        if self.__nItems >= len(self.__a):
            raise Exception("Array full")
        self.__a[self.__nItems] = item
        self.__nItems += 1
    
    #linear search
    def find(self, item):
        for j in range(self.__nItems):
            if self.__a[j] == item:
                return j
            return -1
    
    def search(self, item):
        return self.get(self.find(item))
    
    def delete(self, item):
        for j in range(self.__nItems):
            if self.get(j) == item:
                self.__nItems -= 1
                for k in range(j, self.__nItems):
                    self.__a[k] = self.__a[k+1]
                return True
            
        return False
    
    def traverse(self, function=print):
        for j in range(self.__nItems):
            function(self.__a[j])

    def getMaxNum(self):
        max_num = 0
        for j in range(self.__nItems):
            if isinstance(self.get(j), (int, float)) and self.__a[j] > max_num:
                max_num = self.get(j)
        return max_num if max_num in self.__a else None
    
    def deleteMaxNum(self):
        max_num = 0
        for j in range(self.__nItems):
            if isinstance(self.get(j), (int, float)) and self.__a[j] > max_num:
                max_num = self.get(j)
        val = max_num if max_num in self.__a else None
        self.delete(max_num if max_num in self.__a else None)
        return val
    
    def removeDupes(self):
        unique_array = []
        for j in range(self.__nItems):
            val = self.get(j)
            if val not in unique_array:
                unique_array.append(val)
        self.__a = unique_array
        self.__nItems = len(unique_array)




