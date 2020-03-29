# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return root
        left = root.left
        right = root.right
        self.flatten(left)
        self.flatten(right)
        root.left = None
        if left:
            cur = left
            while cur.right:
                cur = cur.right
            cur.right = right
            root.right = left

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

def print_Tree(root):
    if root:
        print(root.val)
        print_Tree(root.right)

root = create_Tree([1,2,5,3,4,None,6])
s = Solution()
s.flatten(root)
print_Tree(root)
