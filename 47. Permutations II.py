from collections import Counter
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(curr,count):
            if len(curr)==len(nums):
                ans.append(curr[:])
                return
            for num in count:
                if count[num]>0:
                    curr.append(num)
                    count[num]-=1
                    backtrack(curr,count)
                    curr.pop()
                    count[num]+=1
        ans=[]
        backtrack([],Counter(nums))
        return ans
                
        
