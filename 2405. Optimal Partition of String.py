class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans=1
        seen=set()
        for i in range(len(s)):
            if s[i] in seen:
                ans+=1
                seen.clear()
            seen.add(s[i])
        return ans
        -----
class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen=[-1]*26
        count=1
        start=0
        for i in range(len(s)):
            if seen[ord(s[i])-ord('a')]>=start:
                count+=1
                start=i
            seen[ord(s[i])-ord('a')]=i
        return count
        
