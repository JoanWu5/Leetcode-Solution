class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums)<= 0:
            return -1
        left_p = 0
        right_p =len(nums)-1
        while left_p < right_p:
            mid = (right_p-left_p)//2+left_p
            print(left_p,right_p,mid)
            if nums[mid] == target:
                return mid
            if nums[mid]>nums[left_p]:
                #左边有序
                if nums[left_p]<= target <= nums[mid]:
                    right_p = mid
                else:
                    left_p = mid+1
            else:
                #右边有序
                if nums[mid+1] <= target <= nums[right_p]:
                    left_p = mid+1
                else:
                    right_p = mid
        if nums[left_p] == target:
            return left_p
        else:
            return -1


s= Solution()
result = s.search([3,1],1)
print(result)