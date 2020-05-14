from collections import deque
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        #DFS
        # if not board or not board[0]:
        #     return
        # m = len(board)
        # n = len(board[0])
        # if m<=2 or n<=2 :
        #     return
        # def dfs(board,i,j):
        #     if 0<=i<m and 0<=j<n and board[i][j] == 'O':
        #         board[i][j] = 'N'
        #         dfs(board,i,j-1)
        #         dfs(board,i,j+1)
        #         dfs(board,i-1,j)
        #         dfs(board,i+1,j)
        # for i in range(m):
        #     dfs(board,i,0)
        #     dfs(board,i,n-1)

        # for j in range(n):
        #     dfs(board,0,j)
        #     dfs(board,m-1,j)

        # for i in range(m):
        #     for j in range(n):
        #         if board[i][j] == 'O':
        #             board[i][j] = 'X'
        #         elif board[i][j]=='N':
        #             board[i][j] = 'O'       

        #BFS
        if not board or not board[0]:
            return
        m = len(board)
        n = len(board[0])
        if m<=2 or n<=2 :
            return
        q = deque()
        for i in range(m):
            q.append((i,0))
            q.append((i,n-1))
        
        for j in range(n):
            q.append((0,j))
            q.append((m-1,j))
        
        while q:
            i,j = q.popleft()
            if 0<=i<m and 0<=j<n and board[i][j] == 'O':
                board[i][j] = 'N'
                q.append((i,j+1))
                q.append((i,j-1))
                q.append((i-1,j))
                q.append((i+1,j))
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j]=='N':
                    board[i][j] = 'O'  

s = Solution()
board = [['X','X','X','X'],
['X','O','O','X'],
['X','X','O','X'],
['X','O','X','X']]
s.solve(board)
print(board)