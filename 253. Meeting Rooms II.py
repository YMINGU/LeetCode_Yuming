from heapq import *
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        ans=[]
        intervals.sort(key=lambda x:x[0])
        heappush(ans,intervals[0][1])
        for i in intervals[1:]:
            if ans[0]<=i[0]:
                heappop(ans)
            heappush(ans,i[1])
        return len(ans)
        
        
