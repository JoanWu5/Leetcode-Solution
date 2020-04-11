class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        result = []
        result.append([1])
        result.append([1,1])
        dp = [1 for i in range(numRows)]
        for i in range(3,numRows):
            temp = dp.copy()
            for j in range(1,i-1):
                dp[j] = temp[j]+temp[j-1]
            result.append(dp[:i])
        return result

s = Solution()
print(s.generate(5))
        
        
        