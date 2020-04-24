class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix is None or len(matrix) == 0 or matrix[0]is None or len(matrix[0])==0:
            return 0
        m = len(matrix)
        n =  len(matrix[0])
        heights = [[0 for j in range(n)]for i in range(m)]
        result = 0
        for j in range(n):
            if matrix[0][j] == '1':
                heights[0][j] =1
        for i in range(1,m):
            for j in range(n):
                if matrix[i][j] =='1':
                    heights[i][j] = heights[i-1][j]+1
                else:
                    heights[i][j] = 0
        for k in range(m):            
            left = [1]*n
            right = [1]*n
            for i in range(n):
                j = i-1
                while j>=0:
                    if heights[k][j]>=heights[k][i]:
                        left[i] +=left[j]
                        j -=left[j]
                    else:
                        break
            for i in range(n-1,-1,-1):
                j = i+1
                while j<n:
                    if heights[k][j]>=heights[k][i]:
                        right[i]+=right[j]
                        j+=right[j]
                    else:
                        break
            for i in range(n):
                result = max(result,heights[k][i]*(left[i]+right[i]-1))
        return result

s = Solution()
print(s.maximalRectangle([
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]))