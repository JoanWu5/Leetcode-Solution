import collections 
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        #version 1:time limited exceeded
        # lengthp = len(p)
        # result = []
        # for i in range(len(s)-lengthp+1):
        #     str_sort = sorted(s[i:i+lengthp])
        #     print(str_sort)
        #     if str_sort == sorted(p):
        #         result.append(i)
        # return result

        #version 2: sliding window
        result = []
        pcounter = collections.Counter(p)
        scounter = collections.Counter(s[:len(p)-1])
        for i in range(len(p)-1,len(s)):
            scounter[s[i]] +=1
            if scounter == pcounter:
                result.append(i-len(p)+1)
            scounter[s[i-len(p)+1]] -=1
            if scounter[s[i-len(p)+1]] == 0:
                del scounter[s[i-len(p)+1]]       
        return result

s = Solution()
result = s.findAnagrams("cbaebabacd","abc")
print(result)
