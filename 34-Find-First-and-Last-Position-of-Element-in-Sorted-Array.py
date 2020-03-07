class Solution(object):  
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 0:
            return [-1,-1]
        left = 0
        right = len(nums)-1
        result = []
        while left<right:
            mid = (right-left)//2+left
            if nums[mid] == target:
                result.append(mid)
                temp_mid = mid
                while temp_mid+1 <= right:
                    if nums[temp_mid] == nums[temp_mid+1]:
                        temp_mid += 1
                        result.append(temp_mid)
                    else:
                        break
                temp_mid = mid
                while temp_mid-1 >= left:
                    if nums[temp_mid] == nums[temp_mid-1]:
                        temp_mid -=1
                        result.append(temp_mid)
                    else:
                        break
                return [min(result),max(result)]
            elif nums[mid] > target:
                    right = mid-1
            else:
                left = mid+1

        #len(nums)=1 and nums[left] = target
        if nums[left] == target:
            return [left,left]
        else:
            return [-1,-1]

s = Solution()
result = s.searchRange(nums = [2,2], target = 2)
print(result)    


