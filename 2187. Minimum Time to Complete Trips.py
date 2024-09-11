class Solution(object):
    def minimumTime(self, time, totalTrips):
        """
        :type time: List[int]
        :type totalTrips: int
        :rtype: int
        """
        left=1
        right=max(time)*totalTrips
        def timeEnough(given_time):
            trips=0
            for t in time:
                trips+=given_time//t
            return trips>=totalTrips
        while left<=right:
            mid=(left+right)//2
            if timeEnough(mid):
                right=mid-1
            else:
                left=mid+1
        return left
        
