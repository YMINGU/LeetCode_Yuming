class Solution(object):
    def maxRunTime(self, n, batteries):
        """
        :type n: int
        :type batteries: List[int]
        :rtype: int
        """
        left=1
        right=sum(batteries)//n
        while left<right:
            mid=right - (right - left)//2
            extra=0
            for power in batteries:
                extra+=min(power,mid)
            if extra//n>=mid:
                left=mid
            else:
                right=mid-1
        return left
        
