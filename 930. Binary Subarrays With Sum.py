class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        tot=0
        curr=0
        freq={}
        for num in nums:
            curr+=num
            if curr==goal:
                tot+=1
            if curr-goal in freq:
                tot+=freq[curr-goal]
            freq[curr]=freq.get(curr,0)+1
        return tot
        
