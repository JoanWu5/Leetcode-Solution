# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if root:
            level = [root]
            while level:
                result.insert(0,[node.val for node in level])
                temp = []
                for node in level:
                    temp.append(node.left)
                    temp.append(node.right)
                level = [leaf for leaf in temp if leaf]
        return result