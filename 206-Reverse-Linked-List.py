# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #version 1:递归
        if head is None or head.next is None:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p 

        #version 2:迭代
        dummy = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = dummy
            dummy = cur
            cur = temp
        return dummy



        
        