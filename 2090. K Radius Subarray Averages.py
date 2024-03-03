class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k==0:
            return nums
        window_size=2*k+1
        n=len(nums)
        averages=[-1]*n
        if window_size>n:
            return averages
        prefix=[0]*(n+1)
        for i in range(n):
            prefix[i+1]=prefix[i]+nums[i]
        for i in range(k,n-k):
            left,right=i-k,i+k
            subsum=prefix[right+1]-prefix[left]
            average=subsum//window_size
            averages[i]=average
        return averages
        
