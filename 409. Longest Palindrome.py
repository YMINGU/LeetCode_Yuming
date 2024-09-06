from collections import Counter
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=Counter(s)
        flag=False
        res=0
        for freq in count.values():
            if freq%2==0:
                res+=freq
            else:
                res+=freq-1
                flag=True
        if flag:
            return res+1
        return res
--------
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_set=set()
        res=0
        for c in s:
            if c in char_set:
                char_set.remove(c)
                res+=2
            else:
                char_set.add(c)
        if char_set:
            res+=1
        return res
        
