# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def generate(first,last):
            result = []
            for root in range(first,last+1):
                for left in generate(first,root-1):
                    for right in generate(root+1,last):
                        node = TreeNode(root)
                        node.left = left
                        node.right = right
                        result.append(node)
            return result or [None]
        if n==0:
            return []
        return generate(1,n)

s  = Solution()
print(s.generateTrees(3))
        