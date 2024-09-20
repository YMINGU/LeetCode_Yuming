class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        a=[0]*n
        for i in range(n):
            a[(i+k)%n]=nums[i]
        nums[:]=a
--------
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k%=n
        start=count=0
        while count<n:
            curr,prev=start,nums[start]
            while True:
                next_index=(curr+k)%n
                nums[next_index],prev=prev,nums[next_index]
                curr=next_index
                count+=1
                if start==curr:
                    break
            start+=1
-------
