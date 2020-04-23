class Solution():
    def Ksum(self,nums,target):
        def findKsum(l,r,target,K,result,results):
            if r-l+1<K or K<2 or target<nums[l]*K or target>nums[r]*K:
                return
            if K==2:
                while l<r:
                    s = nums[r]+nums[l]
                    if s == target:
                        results.append(result+[nums[l],nums[r]])
                        while l<r and nums[l]==nums[l+1]:
                            l+=1
                        while l<r and nums[r] == nums[r-1]:
                            r-=1
                        l+=1
                        r-=1
                    elif s<target:
                        l+=1
                    else:
                        r-=1
            else:
                for i in range(l,r+1):
                    if i>l and nums[i-1]==nums[i]:
                        continue
                    else:
                        findKsum(i+1,r,target-nums[i],K-1,result+[nums[i]],results)
        nums.sort()
        results = []
        findKsum(0,len(nums)-1,target,4,[],results)
        return results

s = Solution()
print(s.Ksum(nums = [1, 0, -1, 0, -2, 2], target = 0))