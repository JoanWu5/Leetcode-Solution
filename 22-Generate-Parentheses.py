class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def backtract(combination,left,right):
            if len(combination) == 2*n:
                result.append(combination)
                return 
            if left < n:
                backtract(combination+'(',left+1,right)
            if right<left:
                backtract(combination+')',left,right+1)

        result = []
        backtract("",0,0)
        return result

s = Solution()
result = s.generateParenthesis(3)
print(result)