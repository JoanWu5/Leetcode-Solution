# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if root:
            level = [root]
            while level:
                result.append([node.val for node in level])
                temp = []
                for node in level:
                    temp.append(node.left)
                    temp.append(node.right)
                level = [leaf for leaf in temp if leaf]
        return result


def create_Tree(nodeList):
    if nodeList[0] is None:
        return None
    root = TreeNode(nodeList[0])
    Nodes = [root]
    i = 1
    for node in Nodes:
        if node:
            if nodeList[i]:
                node.left = TreeNode(nodeList[i])
            Nodes.append(node.left)
            i+=1
            if i == len(nodeList):
                return root
            if nodeList[i]:
                node.right = TreeNode(nodeList[i])
            Nodes.append(node.right)
            i+=1
            if i == len(nodeList):
                return root

root = create_Tree([3,9,20,None,None,15,7])
s = Solution()
print(s.levelOrder(root))
        