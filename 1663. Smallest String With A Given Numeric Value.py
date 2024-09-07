class Solution(object):
    def getSmallestString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        output=""
        for i in range(n):
            if k-(n-i-1)>=26:
                output=chr(96+26)+output
                k-=26
            else:
                output=chr(96+k-(n-i-1))+output
                k-=(k-(n-i-1))
        return output
        
