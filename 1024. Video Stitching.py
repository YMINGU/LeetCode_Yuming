class Solution(object):
    def videoStitching(self, clips, time):
        """
        :type clips: List[List[int]]
        :type time: int
        :rtype: int
        """
        ends=[0]*time
        for start,end in clips:
            if start<time:
                ends[start]=max(ends[start],end)
        ans=0
        far=0
        next_far=0
        for i in range(time):
            next_far=min(time,max(next_far,ends[i]))
            if i==far:
                ans+=1
                far=next_far
                if i==far:
                    return -1
        return ans
    ----
  
