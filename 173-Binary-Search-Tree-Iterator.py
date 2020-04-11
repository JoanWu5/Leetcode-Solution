# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator(object):
    #version 1:time: 0(n) next():0(1) hasnext():O(1) space:0(n)
    # def __init__(self, root):
    #     """
    #     :type root: TreeNode
    #     """
    #     self.node_sorted = []
    #     self.index = -1
    #     self._inorder(root)
    
    # def _inorder(self,root):
    #     if not root:
    #         return
    #     self._inorder(root.left)
    #     self.node_sorted.append(root.val)
    #     self._inorder(root.right)

    # def next(self):
    #     """
    #     @return the next smallest number
    #     :rtype: int
    #     """
    #     self.index+=1
    #     return self.node_sorted[self.index]

    # def hasNext(self):
    #     """
    #     @return whether we have a next smallest number
    #     :rtype: bool
    #     """
    #     if self.index+1<len(self.node_sorted):
    #         return True
    #     else:
    #         return False

    #version 2: time:hasnext O(1) next:O(1)-O(n) space:O(h)
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self._leftmost(root)
    
    def _leftmost(self,root):
        while root:
            self.stack.append(root)
            root = root.left

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        top_node = self.stack.pop()
        if top_node.right:
            self._leftmost(top_node.right)
        return top_node.val      

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """   
        return len(self.stack)>0


root = TreeNode(7)
root.left = TreeNode(3)
root.right = TreeNode(15)
root.right.right = TreeNode(20)
root.right.left = TreeNode(9)

# Your BSTIterator object will be instantiated and called as such:
iterator = BSTIterator(root);
print(iterator.next())
print(iterator.next())
print(iterator.hasNext())
print(iterator.next())
print(iterator.hasNext())
print(iterator.next())
print(iterator.hasNext())
print(iterator.next())    
print(iterator.hasNext())