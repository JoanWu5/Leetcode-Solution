# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #version 1
        # cur = head
        # lst = []
        # while cur:
        #     lst.append(cur.val)
        #     cur = cur.next
        # lst.sort()
        # dummy = cur = ListNode(0)
        # for i in lst:
        #     node = ListNode(i)
        #     cur.next = node
        #     cur = cur.next
        # return dummy.next

        #version 2:merge sort 
        if head is None or head.next is None:
            return head
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        left = self.sortList(head)
        right = self.sortList(second)
        return self.merge_sort(left,right)

    def merge_sort(self,left,right):
        if left is None or right is None:
            return left or right
        if left.val > right.val:
            left,right = right,left
        head = cur = left
        left = left.next
        while left and right:
            if left.val <right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur = cur.next
        cur.next = right or left
        print(head)
        return head

head = ListNode(4)
head.next = ListNode(2)
head.next.next = ListNode(1)
head.next.next.next = ListNode(3)

s = Solution()
result = s.sortList(head)
while result:
    print(result.val)
    result = result.next



