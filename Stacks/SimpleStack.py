class Stack(object):
    def __init__(self, size):
        self.__stack = [None] * size
        self.__top = -1

    def push(self, item):
        self.__top += 1
        self.__stack[self.__top] = item

    def pop(self):
        top = self.__stack[self.__top]
        self.__stack[self.__top] = None
        self.__top -= 1
        return top
    
    def peek(self):
        if not self.isEmpty():
            return self.__stack[self.__top]
        
    def isEmpty(self):
        return self.__top < 0
    
    def isFull(self):
        return self.__top >= len(self.__stack) -1
    
    def __len__(self):
        return self.__top + 1
    
    def __str__(self):
        ans = "["
        for i in range(self.__top + 1):
            if len(ans) > 1:
                ans += ", "
            ans += str(self.__stack[i])
        ans += "]"
        return ans
            
