from heapq import *
class Solution(object):
    def repeatLimitedString(self, s, repeatLimit):
        """
        :type s: str
        :type repeatLimit: int
        :rtype: str
        """
        heap=[(-ord(char),-count) for char,count in Counter(s).items()]
        heapify(heap)
        res=""
        while heap:
            max_char,max_count=heappop(heap)
            while heap and -max_count>repeatLimit:
                top_char,top_count=heappop(heap)
                res+=chr(-max_char)*repeatLimit+chr(-top_char)
                max_count+=repeatLimit
                if top_count<-1:
                    heappush(heap,(top_char,top_count+1))
            res+=chr(-max_char)*min(-max_count,repeatLimit)
        return res
        
