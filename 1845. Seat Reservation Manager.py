from heapq import *
class SeatManager(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.unreserved=[i for i in range(1,n+1)]
        
        

    def reserve(self):
        """
        :rtype: int
        """
        number=heappop(self.unreserved)
        return number
        

    def unreserve(self, seatNumber):
        """
        :type seatNumber: int
        :rtype: None
        """
        heappush(self.unreserved,seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
