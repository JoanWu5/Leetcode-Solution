class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if self.sub_exist(board,word,i,j,0):
                        return True
        return False


    def sub_exist(self,board,word,starti,startj,index):
        if index == len(word):
            return True
        m = len(board)
        n = len(board[0])
        if starti < 0 or starti >= m or startj <0 or startj >=n or word[index] != board[starti][startj]:
            return False
        board[starti][startj] = '#'
        result =  self.sub_exist(board,word,starti-1,startj,index+1) or \
            self.sub_exist(board,word,starti+1,startj,index+1) or \
            self.sub_exist(board,word,starti,startj-1,index+1) or \
            self.sub_exist(board,word,starti,startj+1,index+1)
        board[starti][startj] = word[index]
        return result

s = Solution()
result = s.exist(board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
],word = "ABCB")
print(result)
