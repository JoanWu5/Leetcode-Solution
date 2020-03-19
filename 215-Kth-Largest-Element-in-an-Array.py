import heapq
import random
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #version 1:sort
        # nums.sort()
        # return nums[-k]

        #version 2:bubble sort O(nk)
        # for i in range(k):
        #     for j in range(len(nums)-i-1):
        #         if nums[j] > nums[j+1]:
        #             nums[j],nums[j+1] = nums[j+1],nums[j]
        # return nums[len(nums)-k]

        #version 3:min-heap:O(n*logk)
        # heap = []
        # for x in nums:
        #     heapq.heappush(heap,x)
        # for i in range(len(nums)-k):
        #     heapq.heappop(heap)
        # return heapq.heappop(heap)

        #version 4:quick selection
        return self.selection(nums,0,len(nums)-1,len(nums)-k)

    def selection(self,nums,left,right,k):
        pivot_index = random.randint(left,right)
        index = self.partition(nums,left,right,pivot_index)
        if index == k:
            return nums[index]
        elif index > k:
            return self.selection(nums,left,index-1,k)
        else:
            return self.selection(nums,index+1,right,k)
    
    def partition(self,nums,left,right,pivot_index):
        pivot = nums[pivot_index]
        nums[right],nums[pivot_index] = nums[pivot_index],nums[right]
        position = left
        for i in range(left,right):
            if nums[i] < pivot:
                nums[i],nums[position] = nums[position],nums[i]
                position +=1
        nums[position],nums[right] = nums[right],nums[position]
        return position



s = Solution()
result = s.findKthLargest([3,2,3,1,2,4,5,5,6], 4)
print(result)