class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        

    def pop(self):
        """
        :rtype: None
        """
        if len(self.stack)>0:
            self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack)>0:
            return self.stack[-1]
        else:
            return None
        
    def getMin(self):
        """
        :rtype: int
        """
        return min(self.stack)
        


# Your MinStack object will be instantiated and called as such:
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())
minStack.pop()
print(minStack.top())
print(minStack.getMin())