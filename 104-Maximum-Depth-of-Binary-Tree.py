# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth = 0
        if root is None:
            return 0
        else:
            depth +=1
        left = root.left
        right = root.right
        depth += max(self.maxDepth(left),self.maxDepth(right))
        return depth

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.right = TreeNode(7)

s = Solution()
print(s.maxDepth(root))

        
        