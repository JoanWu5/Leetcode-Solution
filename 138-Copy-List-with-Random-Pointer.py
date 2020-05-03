# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        nodeDict = {}
        start = Node(0,None,None)
        cur,pointer = start,head
        nodeDict[start] = head

        while pointer:
            node = Node(pointer.val,pointer.next,None)
            nodeDict[pointer] = node
            cur.next = node
            cur = cur.next
            pointer = pointer.next
        
        pointer = head
        while pointer:
            if pointer.random:
                nodeDict[pointer].random = nodeDict[pointer.random]
            pointer = pointer.next
        return start.next

