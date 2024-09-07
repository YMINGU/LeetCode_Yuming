class Solution(object):
    def appendCharacters(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        first=0
        prefix=0
        while first<len(s) and prefix<len(t):
            if s[first]==t[prefix]:
                prefix+=1
            first+=1
        return len(t)-prefix
        
