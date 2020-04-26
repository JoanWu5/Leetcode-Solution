# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #version 1
        # result = []
        # if root:
        #     result.append(root.val)
        #     result.extend(self.preorderTraversal(root.left))
        #     result.extend(self.preorderTraversal(root.right))
        # return result
        
        #version 2:
        result = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                result.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return result
            