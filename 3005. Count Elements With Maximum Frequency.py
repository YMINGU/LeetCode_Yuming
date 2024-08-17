from collections import Counter
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count=Counter(nums)
        high=max(count.values())
        total=0
        for key in count.keys():
            if count[key]==high:
                total+=1
        return total*high
---
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freqs={}
        for num in nums:
            if num in freqs:
                freqs[num]+=1
            else:
                freqs[num]=1
        max_freq=0
        for freq in freqs.values():
            max_freq=max(max_freq,freq)
        freq_max_freq=0
        for freq in freqs.values():
            if freq==max_freq:
                freq_max_freq+=1
        return freq_max_freq*max_freq
        
