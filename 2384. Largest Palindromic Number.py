from collections import Counter
class Solution(object):
    def largestPalindromic(self, num):
        """
        :type num: str
        :rtype: str
        """
        count=Counter(num)
        left=""
        right=""
        odds=""
        for key in sorted(count,reverse=True):
            val=count[key]
            if val%2==0:
                left+=(val//2)*key
                right=(val//2)*key+right
            else:
                left+=(val//2)*key
                right = (key * (val // 2)) + right
                if not odds:
                    odds = key
        v = (left + odds + right).strip("0")
        return v if v else "0"
                
        
