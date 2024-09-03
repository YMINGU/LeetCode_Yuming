from heapq import *
class Solution(object):
    def mostBooked(self, n, meetings):
        """
        :type n: int
        :type meetings: List[List[int]]
        :rtype: int
        """
        unused=list(range(n))
        used=[]
        heapify(unused)
        count=[0]*n
        for start,end in sorted(meetings):
            while used and used[0][0]<=start:
                _,room=heappop(used)
                heappush(unused,room)
            if unused:
                room=heappop(unused)
                heappush(used,[end,room])
            else:
                avail,room=heappop(used)
                heappush(used,[avail+end-start,room])
            count[room]+=1
        return count.index(max(count))
        
