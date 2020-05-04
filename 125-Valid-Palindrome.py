class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == '':
            return True
        left = 0
        right = len(s)-1
        while left<=right:
            #s[left].isalnum()
            while left<=right and (s[left] not in '0123456789' and s[left].lower() not in 'abcdefghijklmnopqrstuvwxyz'):
                left+=1
            while left<=right and (s[right] not in '0123456789' and s[right].lower() not in 'abcdefghijklmnopqrstuvwxyz'):
                right-=1
            if left>right:
                break
            if s[left].lower()!=s[right].lower():
                return False
            else:
                left+=1
                right-=1
        return True

s = Solution()
print(s.isPalindrome("0P"))