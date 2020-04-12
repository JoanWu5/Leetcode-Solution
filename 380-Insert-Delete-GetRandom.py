import random
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.content = set()

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.content:
            return False
        else:
            self.content.add(val)
            return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.content:
            self.content.remove(val)
            return True
        else:
            return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        if self.content:
            nums = list(self.content)
            length = len(self.content)
            index = random.randint(0,length-1)
            return nums[index]
        


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
print(obj.insert(1))
print(obj.remove(2))
print(obj.insert(2))
print(obj.getRandom())