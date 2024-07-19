from heapq import *
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        target=sum(nums)/2
        for i in range(len(nums)):
            nums[i]*=-1
        heapify(nums)
        ans=0
        while target>0:
            num=heappop(nums)
            target+=num/2
            heappush(nums,num/2)
            ans+=1
        return ans
-------
