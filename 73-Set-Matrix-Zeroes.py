class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        #version 1:0(M*N) space:0(m+n)
        # rows = set()
        # cols = set()
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if matrix[i][j] == 0:
        #             rows.add(i)
        #             cols.add(j)
        
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if i in rows or j in cols:
        #             matrix[i][j] =0
        
        
        #version 2 :O(M*N) space:0(1)
        if matrix is None or matrix == []:
            return []
        is_first_col = False
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                is_first_col = True
            for j in range(1,len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if matrix[0][0] == 0:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
        
        if is_first_col:
            for i in range(len(matrix)):
                matrix[i][0] = 0


s =Solution()
matrix = [[1,1,1],[1,0,1],[1,1,1]]
s.setZeroes(matrix)
print(matrix)
        