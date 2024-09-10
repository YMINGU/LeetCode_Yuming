from bisect import *
class Solution(object):
    def maxDistance(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        m=len(nums1)
        n=len(nums2)
        ans=0
        nums2.reverse()
        for i in range(m):
            k=bisect_left(nums2,nums1[i])
            ans=max(ans,n-k-1-i)
        return ans
    -----
  class Solution(object):
    def maxDistance(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        i=0
        j=0
        ans=0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]>nums2[j]:
                i+=1
            else:
                ans=max(ans,j-i)
                j+=1
        return ans
        
