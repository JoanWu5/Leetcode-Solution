class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        d = {}
        def get_key_time (dict, value):
            lst = [k for k, v in dict.items() if v == value]
            return len(lst)
        for task in tasks:
            if task in d:
                d[task] +=1
            else:
                d[task] = 1
        max_key = max(d,key=d.get)
        max_key_times = get_key_time(d,d[max_key])
        interval =max(len(tasks),(d[max_key]-1)*(n+1)+max_key_times)
        return interval

s = Solution()
result = s.leastInterval(tasks = ["A","A","A","B","B","B"], n = 2)
print(result)
