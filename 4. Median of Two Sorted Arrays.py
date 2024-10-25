class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2):
            return self.findMedianSortedArrays(nums2,nums1)
        m,n=len(nums1),len(nums2)
        left,right=0,m
        while left<=right:
            pA=(left+right)//2
            pB=(m+n+1)//2-pA
            maxLeftA=(float("-inf") if pA==0 else nums1[pA-1])
            minRightA=float("inf") if pA==m else nums1[pA]
            maxLeftB=(float("-inf") if pB==0 else nums2[pB-1])
            minRightB=(float("inf") if pB==n else nums2[pB])
            if maxLeftA<=minRightB and maxLeftB<=minRightA:
                if (m+n)%2==0:
                    return (max(maxLeftA,maxLeftB)+min(minRightA,minRightB))/2
                else:
                    return max(maxLeftA,maxLeftB)
            elif maxLeftA>minRightB:
                right=pA-1
            else:
                left=pA+1
        
