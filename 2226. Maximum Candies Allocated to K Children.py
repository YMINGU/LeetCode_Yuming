class Solution(object):
    def maximumCandies(self, candies, k):
        """
        :type candies: List[int]
        :type k: int
        :rtype: int
        """
        s=sum(candies)
        if s<k:
            return 0
        def pile(p):
            piles=0
            for c in candies:
                piles+=c//p
            if piles<k:
                return False
            else:
                return True
        left=1
        right=s//k
        while left<=right:
            mid=(left+right)//2
            if pile(mid):
                left=mid+1
            else:
                right=mid-1
        return right
        
