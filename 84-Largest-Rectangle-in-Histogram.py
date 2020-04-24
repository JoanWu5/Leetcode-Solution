class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n =  len(heights)
        left = [1]*n
        right = [1]*n
        result = 0
        for i in range(n):
            j = i-1
            while j>=0:
                if heights[j]>=heights[i]:
                    left[i] +=left[j]
                    j -=left[j]
                else:
                    break
        for i in range(n-1,-1,-1):
            j = i+1
            while j<n:
                if heights[j]>=heights[i]:
                    right[i]+=right[j]
                    j+=right[j]
                else:
                    break
        for i in range(n):
            result = max(result,heights[i]*(left[i]+right[i]-1))
        return result

s = Solution()
print(s.largestRectangleArea([2,1,5,6,2,3]))
            
