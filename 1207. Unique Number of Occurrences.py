from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count=Counter(arr)
        ans=set(count.values())
        return len(ans)==len(count.keys())
    ---
