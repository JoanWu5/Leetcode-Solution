# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        odd = ListNode(0)
        even = ListNode(0)
        curodd = odd
        cureven = even
        i = 1
        while head:
            if i%2 == 1:
                curodd.next = head
                curodd = curodd.next
            else:
                cureven.next = head
                cureven = cureven.next
            head = head.next
            i +=1
        cureven.next = None
        curodd.next = even.next
        return odd.next



