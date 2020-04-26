class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if root:
            level = [root]
            i = 0
            while level:
                if i%2 == 0:
                    result.append([node.val for node in level])
                else:
                    result.append([node.val for node in reversed(level)])
                temp = []
                for node in level:
                    temp.append(node.left)
                    temp.append(node.right)
                level = [leaf for leaf in temp if leaf]
                i+=1
        return result