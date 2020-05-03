# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = cur = ListNode(0)
        dummy.next = head
        for i in range(1,m):
            cur = cur.next
        pm = cur
        pend = pm.next
        cur = cur.next
        dummy2 = ListNode(0)
        for i in range(m,n+1):
            temp = cur.next
            cur.next = dummy2
            dummy2 = cur
            cur = temp
        pm.next = dummy2
        pend.next = cur
        return dummy.next