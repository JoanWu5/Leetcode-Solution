class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = []
        self.dfs(s,[],result)
        return result
    
    def dfs(self,s,path,result):
        if not s:
            result.append(path.copy())
            return 
        for i in range(1,len(s)+1):
            if s[:i] == s[i-1::-1]:
                path.append(s[:i])
                self.dfs(s[i:],path,result)
                path.pop()

s = Solution()
print(s.partition('aab'))