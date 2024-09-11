
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo=0
        hi=len(nums)-1
        while lo<hi:
            mid=lo+(hi-lo)//2
            even=(hi-mid)%2==0
            if nums[mid+1]==nums[mid]:
                if even:
                    lo=mid+2
                else:
                    hi=mid-1
            elif nums[mid-1]==nums[mid]:
                if even:
                    hi=mid-2
                else:
                    lo=mid+1
            else:
                return nums[mid]
        return nums[lo]
        
