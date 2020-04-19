class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        result = []
        line = ''
        for word in words:
            if len(line) + len(word) <maxWidth:
                line +=word
            else:
                result.append(line)
                line = ''
                line += word
        if len(line) != 0:
            result.append(line)
        return result

s = Solution()
print(s.fullJustify(["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"],20))
