# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.result = None
        
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        def recurse_Tree(current_node):
            if not current_node:
                return False
            left = recurse_Tree(current_node.left)
            right = recurse_Tree(current_node.right)
            mid = current_node == p or current_node == q
            if mid + left + right>=2:
                self.result = current_node
            return mid or left or right
        recurse_Tree(root)
        return self.result

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


s = Solution()
root = create_Tree( [3,5,1,6,2,0,8,None,None,7,4])
result = s.lowestCommonAncestor(root,root.left,root.left.right)
print(result.val)

