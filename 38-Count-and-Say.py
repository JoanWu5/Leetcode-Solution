class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        result = '1'
        for ni in range(2,n+1):
            i = 0
            count = 1
            temp = result
            result = ''
            while i<len(temp)-1:
                if temp[i] == temp[i+1]:
                    count+=1
                    i+=1
                else:
                    result+=str(count)+temp[i]
                    count = 1
                    i+=1
            result+=str(count)+temp[i]
        return result

s = Solution()
print(s.countAndSay(2))
