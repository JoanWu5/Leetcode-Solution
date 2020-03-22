class Solution(object):
    dp = {}
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 1
        if n in self.dp:
            return self.dp[n]
        result = 0
        for i in range(1,n+1):
            result += self.numTrees(i-1)*self.numTrees(n-i)
        self.dp[n] = result
        return result

s = Solution()
result = s.numTrees(4)
print(result)

        