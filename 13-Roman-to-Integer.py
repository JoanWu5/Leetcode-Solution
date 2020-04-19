class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        map_roman={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        if s is None or s =='':
            return 0
        if len(s) == 1:
            return map_roman[s[0]]
        result = map_roman[s[-1]]
        max_item = map_roman[s[-1]]
        for i in range(len(s)-2,-1,-1):
            if map_roman[s[i]] >= max_item:
                result +=map_roman[s[i]]
                max_item = map_roman[s[i]]
            else:
                result -=map_roman[s[i]]
        return result

s = Solution()
print(s.romanToInt('MCMXCIV'))
