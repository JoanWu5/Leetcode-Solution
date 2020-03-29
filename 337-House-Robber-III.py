# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return max(self.dfs(root))

    def dfs(self,root):
        if not root:
            return (0,0)
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        return (root.val+left[1]+right[1],max(left[0],left[1])+max(right[0],right[1]))

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

root = create_Tree( [3,4,5,1,3,None,1])
s = Solution()
print(s.rob(root))
