class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lower_bound=self.find(nums,target,True)
        if lower_bound==-1:
            return [-1,-1]
        upper_bound=self.find(nums,target,False)
        return [lower_bound,upper_bound]
    def find(self,nums,target,isFirst):
        n=len(nums)
        left,right=0,n-1
        while left<=right:
            mid=int((left+right)/2)
            if nums[mid]==target:
                if isFirst:
                    if mid==left or nums[mid-1]<target:
                        return mid
                    right=mid-1
                else:
                    if mid==right or nums[mid+1]>target:
                        return mid
                    left=mid+1
            elif nums[mid]>target:
                right=mid-1
            else:
                left=mid+1
        return -1
        
