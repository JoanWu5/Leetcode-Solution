# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = 0
        if root:
            result +=self.max_depth(root.left,0)+self.max_depth(root.right,0)
            result = max(self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right),result)
        return result
        
    def max_depth(self,root,depth):
        if root:
            depth = max(self.max_depth(root.left,depth),self.max_depth(root.right,depth))+1
            return depth
        else:
            return 0
        

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.right= TreeNode(4)

s = Solution()
print(s.max_depth(root,0))
print(s.diameterOfBinaryTree(root))

