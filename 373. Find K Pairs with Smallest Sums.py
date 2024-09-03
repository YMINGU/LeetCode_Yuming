from heapq import *
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        m=len(nums1)
        n=len(nums2)
        ans=[]
        seen=set()
        heap=[(nums1[0]+nums2[0],(0,0))]
        seen.add((0,0))
        count=0
        while k>0 and heap:
            val,(i,j)=heappop(heap)
            ans.append((nums1[i],nums2[j]))
            if i+1<m and (i+1,j) not in seen:
                heappush(heap,(nums1[i+1]+nums2[j],(i+1,j)))
                seen.add((i+1,j))
            if j+1<n and (i,j+1) not in seen:
                heappush(heap,(nums1[i]+nums2[j+1],(i,j+1)))
                seen.add((i,j+1))
            k-=1
        return ans
        
