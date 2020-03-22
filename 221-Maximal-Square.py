class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        #version 1:dp
        # if matrix == []:
        #     return 0
        # max_length = 0
        # m = len(matrix)
        # n = len(matrix[0])
        # dp = [[0 for j in range(n)] for i in range(m)]
        # for i in range(m):
        #     if matrix[i][0] == '1':
        #         dp[i][0] =1
        #         max_length =1

        # for j in range(n):
        #     if matrix[0][j] =='1':
        #         dp[0][j] = 1
        #         max_length =1
        #
        # if m==1 or n==1:
        #     return max_length**2

        # for i in range(1,m):
        #     for j in range(1,n):
        #         if matrix[i][j] =='1':
        #             dp[i][j] = min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])+1
        #             max_length = max(max_length,dp[i][j])
        # return max_length**2

        #version 2:
        if matrix == []:
            return 0
        max_length = 0
        m = len(matrix)
        n = len(matrix[0])
        dp = [0 for j in range(n)]

        for j in range(n):
            if matrix[0][j] =='1':
                dp[j] = 1
                max_length =1

        if m==1 or n==1:
            return max_length**2

        for i in range(1,m):
            temp = dp.copy()
            print("temp",temp)
            if matrix[i][0] == '1':
                dp[0] = 1
                max_length = max(max_length,1)
            else:
                dp[0] = 0
            for j in range(1,n):
                if matrix[i][j] =='1':
                    dp[j] = min(dp[j-1],dp[j],temp[j-1])+1
                    max_length = max(max_length,dp[j])
                else:
                    dp[j] = 0
        return max_length**2
s = Solution()
result = s.maximalSquare(
[["1","0","1","0"],["1","0","1","1"],["1","0","1","1"],["1","1","1","1"]])
print(result)
             