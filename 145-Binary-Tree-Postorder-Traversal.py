# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #version 1:
        # result = []
        # if root:
        #     result.extend(self.postorderTraversal(root.left))
        #     result.extend(self.postorderTraversal(root.right))
        #     result.append(root.val)
        # return result

        #version 2:
        result = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                result.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        return result[::-1]