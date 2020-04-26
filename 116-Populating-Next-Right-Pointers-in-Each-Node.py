"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        #version 1 ：
        # p = root
        # first = None
        # while p:
        #     if first is None:
        #         first = p.left
        #     if p.left:
        #         p.left.next = p.right
        #     else:
        #         break
        #     if p.next:
        #         p.right.next = p.next.left
        #         p = p.next
        #     else:
        #         p = first
        #         first = None
        # return root

        #version 2:
        p = root
        if p and p.left and p.right:
            p.left.next = p.right
            if p.next:
                p.right.next = p.next.left
            self.connect(p.left)
            self.connect(p.right)
        return root


                
                
