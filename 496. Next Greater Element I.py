class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[0]*len(nums1)
        for i in range(len(nums1)):
            j=0
            while nums2[j]!=nums1[i]:
                j+=1
            if j==len(nums2)-1:
                ans[i]=-1
                continue
            for j in range(j+1,len(nums2)):
                if j==len(nums2)-1 and nums2[j]<=nums1[i]:
                    ans[i]=-1
                elif nums2[j]>nums1[i]:
                    ans[i]=nums2[j]
                    break
        return ans
  ---------------------
from collections import defaultdict
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        Map=defaultdict()
        stack=[]
        ans=[0]*len(nums1)
        for j in range(len(nums2)):
            while stack and stack[-1]<nums2[j]:
                curr=stack.pop()
                Map[curr]=nums2[j]
            stack.append(nums2[j])
        while stack:
            curr=stack.pop()
            Map[curr]=-1
        for i in range(len(nums1)):
            ans[i]=Map[nums1[i]]
        return ans
            
        
