# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        #version 1: two pass
        # cur = head
        # count = 0
        # while cur:
        #     count +=1
        #     cur = cur.next
        # cur = head
        # count1 = 0
        # if n== count:
        #     return head.next
        # while cur:
        #     count1 +=1
        #     if count1 == count-n:
        #         cur.next = cur.next.next
        #         return head
        #     cur = cur.next

        #version 2:one pass
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = dummy
        for i in range(n+1):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next
        

node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)

s = Solution()
node1 = s.removeNthFromEnd(node,3)
while node1:
    print(node1.val)
    node1 = node1.next