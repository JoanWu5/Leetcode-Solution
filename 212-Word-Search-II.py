class TrieNode():
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie():
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self,word):
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()
            node = node.children[w]
        node.isEnd = True

    def search(self,word):
        node = self.root
        for w in word:
            node = node.children.get(w)
            if not node:
                return False
        return node.isEnd

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        result = []
        trie = Trie()
        node = trie.root
        for w in words:
            trie.insert(w)
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board,node,i,j,"",result)
        return result
    
    def dfs(self,board,node,i,j,path,result):
        if node.isEnd:
            result.append(path)
            node.isEnd = False
        if i<0 or i>=len(board) or j <0 or j>=len(board[0]):
            return
        temp = board[i][j]
        node = node.children.get(temp)
        if not node:
            return
        board[i][j] = '#'
        self.dfs(board,node,i+1,j,path+temp,result)
        self.dfs(board,node,i-1,j,path+temp,result)
        self.dfs(board,node,i,j-1,path+temp,result)
        self.dfs(board,node,i,j+1,path+temp,result)
        board[i][j] = temp

s= Solution()
print(s.findWords(board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
],words = ["oath","pea","eat","rain"]))