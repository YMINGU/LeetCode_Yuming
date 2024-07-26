class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        ans=[]
        for query in queries:
            count=0
            for num in nums:
                if query>=num:
                    query-=num
                    count+=1
                else:
                    break
            ans.append(count)
        return ans

----
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        def binary_search(arr,target):
            left=0
            right=len(arr)-1
            while left<=right:
                mid=(left+right)//2
                if arr[mid]<=target:
                    left=mid+1
                else:
                    right=mid-1
            return left
        nums.sort()
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
        ans=[]
        for query in queries:
            i=binary_search(nums,query)
            ans.append(i)
        return ans
        
