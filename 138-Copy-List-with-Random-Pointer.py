# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
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
        newHead,pointer = start,head
        nodeDict[start] = head

        while pointer:
            node = Node(pointer.val,pointer.next,None)
            nodeDict[pointer] = node
            newHead.next = node
            newHead,pointer = newHead.next,pointer.next

        pointer = head
        while pointer:
            if pointer.random:
                nodeDict[pointer].random = nodeDict[pointer.random]
            pointer = pointer.next 

        return start.next
       