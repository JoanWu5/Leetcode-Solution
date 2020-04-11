class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.c = {}
        self.end = False

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        node = self
        for w in word:
            if w not in node.c:
                node.c[w] = Trie()
            node = node.c[w]
        node.end = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self
        for w in word:
            if w not in node.c:
                return False
            node = node.c[w]
        if node.end:
            return True
        return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self
        for w in prefix:
            if w not in node.c:
                return False
            node = node.c[w]
        return True
        


# Your Trie object will be instantiated and called as such:
trie = Trie();

trie.insert("apple")
print(trie.search("apple"))   
print(trie.search("app"))
print(trie.startsWith("app"))
trie.insert("app")   
print(trie.search("app"))