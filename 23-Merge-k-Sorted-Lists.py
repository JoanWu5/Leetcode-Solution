from queue import PriorityQueue
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        #O(Nlogk)
        # dummy = cur = ListNode(0)
        # q = PriorityQueue()
        # for l in lists:
        #     if l:
        #         q.put((l.val,id(l),l))
        # while q.qsize()>0:
        #     cur.next = q.get()[2]
        #     cur = cur.next
        #     if cur.next:
        #         q.put((cur.next.val,id(cur.next),cur.next))
        # return dummy.next
        interval = 1
        while interval<len(lists):
            for i in range(0,len(lists)-interval,2*interval):
                lists[i] = self.mergeTwoLists(lists[i],lists[i+interval])
            interval *=2
        return lists[0] if len(lists) else lists
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None or l2 is None:
            return l1 or l2
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val<l2.val:
                cur.next = l1
                l1 = l1.next
                cur = cur.next
            else:
                cur.next = l2
                l2 = l2.next
                cur = cur.next
        if l1 or l2:
            cur.next = l1 or l2
        return dummy.next

s = Solution()
def create_Listnode(nums):
    dummy= cur = ListNode(0)
    for num in nums:
        cur.next = ListNode(num)
        cur = cur.next
    return dummy.next

head1 = create_Listnode([1,4,5])
head2 = create_Listnode([1,3,4])
head3 = create_Listnode([2,6])
result = s.mergeKLists([head1,head2,head3])
while result:
    print(result.val)
    result = result.next