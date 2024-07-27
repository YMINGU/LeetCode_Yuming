class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def check(m):
            res=0
            split=0
            for num in nums:
                if res+num<=m:
                    res+=num
                else:
                    res=num
                    split+=1
            return (split+1)<=k
        left=max(nums)
        right=sum(nums)
        while left<=right:
            mid=(left+right)//2
            if check(mid):
                right=mid-1
            else:
                left=mid+1
        return left
        
