class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        #version 1: O(n^2)
        # max_length = 0
        # lst = []
        # for i in range(len(s)):
        #     count = 1
        #     lst.append(s[i])
        #     for j in range(i+1,len(s)):
        #         if s[j] in lst:
        #             break
        #         lst.append(s[j])
        #         count +=1
        #     max_length = max(max_length,count)
        #     lst = []
        # return max_length

        #version 2: sliding window
        # max_length = 0
        # lst = []
        # for i in s:
        #     if not i in lst:
        #         lst.append(i)
        #         max_length = max(max_length,len(lst))
        #     else:
        #         k = lst.index(i)
        #         if k == len(lst)-1:
        #             lst = []
        #         else:
        #             lst = lst[k+1:]
        #         lst.append(i)
        # return max_length

        #version 3:hashmap,sliding window
        dict = {}
        max_length = 0
        start = 0
        for i,value in enumerate(s):
            if value in dict:
                before_index = dict[value]+1
                if before_index>start:
                    start = before_index
            length = i-start+1
            if length>max_length:
                max_length = length
            dict[value] = i
        
        return max_length



s = Solution()
result = s.lengthOfLongestSubstring("abcabcf")
print(result)


            