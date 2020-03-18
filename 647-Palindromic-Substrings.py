class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        #version 1 
        # result = 0
        # for center in range(2*len(s)-1):
        #     left = center//2
        #     right = left+center%2
        #     while left>=0 and right<len(s) and s[left] ==s[right]:
        #         left -=1
        #         right +=1
        #         result+=1
        # return result

        #version 2:dp
        dp = [[False for i in range(len(s))]for j in range(len(s))]
        count = 0

        for i in range(len(s)-1,-1,-1):
            dp[i][i] =  True
            count +=1
            for j in range(i+1,len(s)):
                if j == i+1 and s[i] == s[j]:
                    dp[i][j] = True
                    count +=1
                if j>i+1 and dp[i+1][j-1] and s[i] == s[j]:
                    dp[i][j] = True
                    count +=1
        return count

s = Solution()
result = s.countSubstrings("aaa")
print(result)
