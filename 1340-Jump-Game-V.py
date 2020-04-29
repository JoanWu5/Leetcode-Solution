class Solution(object):
    def maxJumps(self, arr, d):
        """
        :type arr: List[int]
        :type d: int
        :rtype: int
        """
        result = [0]*len(arr)
        def dp(i):
            if result[i]:
                return result[i]
            result[i] =1
            for di in [-1,1]:
                for j in range(i+di,i+d*di+di,di):
                    if 0<=j<len(arr) and arr[j]<arr[i]:
                        result[i] = max(result[i],dp(j)+1)
                    else:
                        break
            return result[i]
        return max(dp(i) for i in range(len(arr)))

s = Solution()
print(s.maxJumps([6,4,14,6,8,13,9,7,10,6,12],2))
