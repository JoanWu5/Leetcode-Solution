class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        #version 1:找规律
        # i = 0 
        # j = 0
        # n = len(matrix[0])
        # if n>=1 :
        #     if n%2 == 0:
        #         k = n/2
        #     else:
        #         k = n/2+1
        #     print(k)
        #     while i < int(k):
        #         for j in range(i,n-i-1):
        #             print(i,j)
        #             matrix[i][j],matrix[j][n-1-i],matrix[n-1-i][n-1-j],matrix[n-1-j][i]= \
        #             matrix[n-1-j][i],matrix[i][j],matrix[j][n-1-i],matrix[n-1-i][n-1-j]
        #         i +=1

        #先做矩阵转置（即沿着对角线翻转），然后每个列表翻转
        n= len(matrix[0])
        for i in range(n):
            for j in range(i,n):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        
        for m in matrix:
            m.reverse()
                
        
s = Solution()
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
s.rotate(matrix)
print(matrix)
            