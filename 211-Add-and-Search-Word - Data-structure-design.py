class Trie:
    def __init__(self):
        self.children = {}
        self.isEnd = False
    
class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Trie()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = Trie()
            node = node.children[w]
        node.isEnd = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        stack = [(self.root,word)]
        while stack:
            node,w = stack.pop()
            if not w:
                if node.isEnd:
                    return True
            elif w[0] == '.':
                for n in node.children.values():
                    stack.append((n,w[1:]))
            else:
                if w[0] in node.children:
                    n = node.children[w[0]]
                    stack.append((n,w[1:]))
        return False
        
# Your WordDictionary object will be instantiated and called as such:
s= WordDictionary()
s.addWord('bad')
s.addWord('dad')
s.addWord('mad')
print(s.search('pad'))
print(s.search('.ad'))
print(s.search('..b'))