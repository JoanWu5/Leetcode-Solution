import collections
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        #O(m*n) space:O(1)
        # neighbors = [(1,0),(1,-1),(1,1),(0,1),(0,-1),(-1,0),(-1,-1),(-1,1)]
        # m = len(board)
        # n = len(board[0])
        # for row in range(m):
        #     for col in range(n):
        #         live_neighbors = 0 
        #         for neighbor in neighbors:
        #             r = row + neighbor[0]
        #             c = col + neighbor[1]
        #             if r< m and r>=0 and c<n and c>=0 and abs(board[r][c])==1:
        #                 live_neighbors +=1
        #         if board[row][col] == 1 and (live_neighbors<2 or live_neighbors>3):
        #             board[row][col] = -1
        #         if board[row][col] == 0 and live_neighbors == 3:
        #             board[row][col] = 2
        
        # for row in range(m):
        #     for col in range(n):
        #         if board[row][col] >0:
        #             board[row][col] = 1
        #         else:
        #             board[row][col] = 0
        live = {(i,j) for i ,row in enumerate(board) for j,live in enumerate(row) if live}
        live = self.gameOfLifeInfinite(live)
        for i,row in enumerate(board):
            for j in range(len(row)):
                row[j] = int((i,j) in live)

    def gameOfLifeInfinite(self,live):
        ctr = collections.Counter((I,J) for i,j in live 
                                            for I in range(i-1,i+2)
                                                for J in range(j-1,j+2)   
                                                if I!= i and J!= j)
        return {ij for ij in ctr if ctr[ij] == 3 or ctr[ij]==2 and ij in live}

s = Solution()
board = [
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
s.gameOfLife(board)
print(board)

