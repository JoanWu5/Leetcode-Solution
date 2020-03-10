import collections
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        #version 1:
        # def get_sort(str):
        #     return "".join(sorted(str))

        # d = {}
        # for i in range(len(strs)):
        #     sorted_string = get_sort(strs[i])
        #     if sorted_string in d:
        #         d[sorted_string] +="#"+strs[i]
        #     else:
        #         d[sorted_string] = strs[i]
        # result = []
        # for key,value in d.items():
        #     result.append(value.split("#"))
        # return result
        
        #version 2:use defaultdict
        # ans = collections.defaultdict(list)
        # for s in strs:
        #     ans[tuple(sorted(s))].append(s)
        # return ans.values()

        #version 3:
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c)-ord('a')] +=1 
            ans[tuple(count)].append(s)
        return ans.values()

s = Solution()
result = s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print(result)

