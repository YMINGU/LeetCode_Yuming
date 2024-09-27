class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        for num in nums2:
            pos=bisect.bisect_left(nums1[:m],num)
            nums1.insert(pos,num)
            nums1.pop()
            m+=1
        
----------
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[i+m]=nums2[i]
        nums1.sort()
        
        
