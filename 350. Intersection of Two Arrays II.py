from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        count1=Counter(nums1)
        count2=Counter(nums2)
        for num in count1.keys():
            if num in count2.keys():
                ans+=[num]*min(count1[num],count2[num])
        return ans
  ------
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1=sorted(nums1)
        nums2=sorted(nums2)
        i,j=0,0
        ans=[]
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<nums2[j]:
                i+=1
            elif nums1[i]>nums2[j]:
                j+=1
            else:
                ans.append(nums1[i])
                i+=1
                j+=1
        return ans
        
