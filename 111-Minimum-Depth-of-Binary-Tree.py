# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth = 0
        if root is None:
            return 0
        depth+=1
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if left == 0:
            depth+=right
        elif right ==0:
            depth+=left
        else:
            depth+=min(left,right)
        return depth