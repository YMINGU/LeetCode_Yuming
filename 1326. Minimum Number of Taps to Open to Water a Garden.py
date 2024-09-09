class Solution(object):
    def minTaps(self, n, ranges):
        """
        :type n: int
        :type ranges: List[int]
        :rtype: int
        """
        max_reach=[0]*(n+1)
        for i in range(len(ranges)):
            start=max(0,i-ranges[i])
            end=min(n,i+ranges[i])
            max_reach[start]=max(max_reach[start],end)
        taps=0
        curr_end=0
        next_end=0
        for i in range(n+1):
            if i>next_end:
                return -1
            if i>curr_end:
                taps+=1
                curr_end=next_end
            next_end=max(next_end,max_reach[i])
        return taps
        
