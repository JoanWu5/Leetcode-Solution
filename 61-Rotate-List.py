# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or head.next is None or k == 0:
            return head
        length = 0
        cur = head
        while cur:
            length+=1
            cur = cur.next
        k = length - k%length
        if k == length:
            return head
        dummy = cur = ListNode(0)
        dummy.next = head
        for _ in range(k):
            cur = cur.next
        temp = cur.next
        cur.next = None
        dummy.next = temp
        cur = temp
        while cur.next:
            cur = cur.next
        cur.next = head
        return dummy.next
            