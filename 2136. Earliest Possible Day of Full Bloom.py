class Solution(object):
    def earliestFullBloom(self, plantTime, growTime):
        """
        :type plantTime: List[int]
        :type growTime: List[int]
        :rtype: int
        """
        curr=0
        res=0
        indices=sorted(range(len(plantTime)),key=lambda x:-growTime[x])
        for i in indices:
            curr+=plantTime[i]
            res=max(res,curr+growTime[i])
        return res
        
